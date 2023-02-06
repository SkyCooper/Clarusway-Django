from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

#? djangonun default permission modeli
from rest_framework.permissions import DjangoModelPermissions
# https://www.django-rest-framework.org/api-guide/permissions/#djangomodelpermissions

# admin panelde herhangi bir user'a user bazında permission ataması yapılabiliyor,
# admin panelde Users'tan bir kullanıcı üzerine tıklayınca
# Groups ve User permissions özellikleri ayarlanabiliyor,
# User permissions ile mevcut bütün CRUD işlemlerinden istenilen tek tek seçilebilir,

# Groups ile bir grup oluşturulup, CRUD işlemlerinden istenilen tek tek seçilebilir
# ve user o gruba tanırsa, gruba izin verilen işemleri yapabilir,

# superuser olarak create edilen admin
# veya sonradan superuser olarak işaretlenen user bütün CRUD işlemlerini yapmaya izinlidir.

# Create your views here.
class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["name"]
    filterset_fields = ["name"]
    
    #? djangonun default permission modeli
    permission_classes = [DjangoModelPermissions]
    
    #! view içerisinde faklı durumlara göre farklı serializer kullanma,
    #? gelen sorguda name varsa/yoksa oan göre farklı serializer kullanacak,
    #? onun için kullanılacak serializerı seçen, get_serializer_class metodu override ediliyor,
    def get_serializer_class(self):
        if self.request.query_params.get("name"):
            #? sorgudan name varsa;
            return CategoryProductSerializer
        #? yoksa parentten aynısını kullan; (yani CategorySerializer)
        return super().get_serializer_class()
    

class BrandView(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [SearchFilter]
    search_fields = ["name"]
    permission_classes = [DjangoModelPermissions]
    

class FirmView(ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    filter_backends = [SearchFilter]
    search_fields = ["name"]
    permission_classes = [DjangoModelPermissions]
    

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ["category", "brand"]
    search_fields = ["name"]
    permission_classes = [DjangoModelPermissions]
    

class PurchasesView(ModelViewSet):
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    #? permission
    permission_classes = [DjangoModelPermissions]
    
    #? filter
    filterset_fields = ["product", "firm"]
    
    #? search
    # search_fields = ["quantity"]
    search_fields = ["firm__name"]      #? firm ForeinKey olduğundan onun ismine ulaşmak için __(ikialtçizgi) kullanıyoruz.
    # search_fields=['^firm__name']       #* baş harfine göre arama yapmak için,
    ordering_fields = ['quantity']      #* filter boxta hangi seçenekler çıksın istiyorsanız onu yazıyorsunuz
    ordering = ['price']                #* default olarak ilk açıldığında buraya yazdığımıza göre sıralıyor
    
    
    #? product stock miktarını yapılan purchase'e göre hesaplamak için,(quantity kadar arttırıcaz)
    #? ModelViewSet içinden --> CreateModelMixin --> def create metodunu override ediyoruz,
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #? gelen data valid ise ve serializerden geçtiyse stock miktarını hesaplayabiliriz,
        
        #! #############  ADD Product Stock ############
        #bir alım yapıldı (purchase), bunu yani istek yapılan data'yı bir değişkene atıyoruz,
        purchase = request.data
        
        #hangi product stoğu güncellenecek,
        #alım yapılan(purchase) ürünün product_id'si ile ürün tablosundaki id'si aynı olan ürünü bulup değişkene atıyoruz,
        product = Product.objects.get(id=purchase["product_id"])
        
        #bu ürünün stock miktarını alım yapılan ürün miktarı kadar arttırıyoruz
        product.stock += purchase["quantity"]
        
        # ve ürünü DB'ye kayıt ediyoruz 
        product.save()
        #! #############################################
        
        #? bundan sonrası aynı, stoğu güncellenmiş olarak serializerdan geçiriyoruz.
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    #? bu işlemi hangi user yaptı
    # önceki projelerde bunu serilaizerde create metodunu override ederek yapmıştık, (flightApp, rentCar)
    def perform_create(self, serializer):
        #? aslında sadece save var, böyle olursa null gönderir,
        # serializer.save()
        #? içerisine user fieldi eklenerek daha kolay yapılabiliyor. 
        serializer.save(user=self.request.user)
        
    #? yapılan purchase güncellenmesi;
    #? mevcut quantity'den büyükse stock artacak, küçükse azalacak
    #? ModelViewSet içinden --> UpdateModelMixin --> def update metodunu override ediyoruz,
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        #? gelen data valid ise ve serializerden geçtiyse stock miktarını güncelleyebiliriz,
        
        #! #############  UPDATE Product Stock ############
        #bir alım yapıldı (purchase), bunu yani istek yapılan data'yı bir değişkene atıyoruz,
        purchase = request.data
        
        #hangi product stoğu güncellenecek,
        #alım yapılan(purchase) ürünün product_id'si ile ürün tablosundaki id'si aynı olan ürünü bulup değişkene atıyoruz,
        product = Product.objects.get(id=instance.product_id)
        
        #güncellenen yeni quantity'den mevcut quantity çıkarıldı fark bulundu
        fark = purchase["quantity"] - instance.quantity
        
        #mevcut stoğa eklendi, artış varsa pozitif olacak ve stok artacak azalma varsa negatif olacak stok azalacak
        product.stock += fark
        
        # ve ürünü DB'ye kayıt ediyoruz 
        product.save()
        #! #############################################
        
        #? bundan sonrası aynı, stoğu güncellenmiş olarak serializerdan geçiriyoruz.
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
    
    #? yapılan purchase silinmesi;
    #? mevcut quantity'den stoktan çıkarılacak
    #? ModelViewSet içinden --> DestroyModelMixin --> def destroy metodunu override ediyoruz,
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        #! #############  DELETE Product Stock ############
        #hangi product stoğu güncellenecek,
        #alım yapılan(purchase) ürünün product_id'si ile ürün tablosundaki id'si aynı olan ürünü bulup değişkene atıyoruz,
        product = Product.objects.get(id=instance.product_id)
        
        #silinen purchase quantity kadar stoktan çıkarılır.
        product.stock -= instance.quantity
        product.save()
        #! #############################################
        
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class SalesView(ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        sale = serializer.save()
        sale.price_total = sale.quantity * sale.price
        sale.save()
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
#! Abdullah hocanın çift kayıt yapan view kodu düzenlenmiş hali,  
    
    # def create(self, request, *args, **kwargs):
    #     response = super().create(request, *args, **kwargs)
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
        
    #     quantity = serializer.validated_data.get('quantity')
    #     price = serializer.validated_data.get('price')
    #     response.data['price_total'] = quantity * price
    #     return response
    

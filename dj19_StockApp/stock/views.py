from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter, OrderingFilter


# Create your views here.
class CategoryMVS(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class BrandMVS(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    

class FirmMVS(ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    

class ProductMVS(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    

class PurchasesMVS(ModelViewSet):
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer
    
    #? filter
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["product",]
    
    #? search
    # search_fields = ["quantity"]
    search_fields = ["firm__name"]      #? firm ForeinKey olduğundan onun ismine ulaşmak için __(ikialtçizgi) kullanıyoruz.
    # search_fields=['^firm__name']       #* baş harfine göre arama yapmak için,
    ordering_fields = ['quantity']      #* filter boxta hangi seçenekler çıksın istiyorsanız onu yazıyorsunuz
    ordering = ['price']                #* default olarak ilk açıldığında buraya yazdığımıza göre sıralıyor
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        purchase = serializer.save()
        purchase.price_total = purchase.quantity * purchase.price
        purchase.save()
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class SalesMVS(ModelViewSet):
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
    

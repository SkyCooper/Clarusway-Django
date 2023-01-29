from .serializers import CarSerializer, ReservationSerializer
from .models import Car, Reservation
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .permissions import IsStafforReadOnly
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone

# Create your views here.

class CarMVS(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsStafforReadOnly,)
    
    #! task, can select start and end date and see the list of available cars on selected dates.
    #! availibity staff ise bütün araçları görsün, client sadece müsait olanları görsün diye,
    #? https://yolcu360.com/tr/rent-a-car/ankara-esenboga-havalimani-arac-kiralama/?from=2023-01-27&to=2023-01-29
    #? mesela biz bir tarih aralığı seçince url frontend tarafından yukarıdaki gibi oluşur,
    #? ?from=2023-01-27&to=2023-01-29 soru işaretinden sonra gelenler PARAMETREDİR, from/to, start/end isim önemli değil
    #? girilen bu tarih aralığını yakalamak için  request.query_params.get() kullanılıyor,
    #? query_params bir dictionary olduğundan key'i start veya end olan değerleri alıyoruz,
    #* http://127.0.0.1:8000/api/car/?start=2023-01-15&end=2023-01-20 böyle bir endpoint yazıyoruz bakmak için,
    
    def get_queryset(self):
        # staff ise bütün araçları görsün,
        if self.request.user.is_staff:
            queryset = super().get_queryset()
            
        # client sadece müsait olanları görsün
        else:
            queryset = super().get_queryset().filter(availibity=True)
        
        # ve sadece seçtiği tarih aralığındaki müsait araçları görsün
        # bunun için frontend tarafından gönderilen parametleri yakalıyoruz,
        start = self.request.query_params.get("start")
        # print("start", start)
        end = self.request.query_params.get("end")
        # print(end)
        
        #? Q parametresi bitwise operatörü ile kullanılır, and/or yerine & veya | kullanılır.
        #? available olanlar için bir condition yazıyoruz
        #* https://books.agiliq.com/projects/django-orm-cookbook/en/latest/query_relatedtool.html
        condition1 = Q(start_date__lt=end) #less than 
        condition2 = Q(end_date__gt=start) #greater than
        
        #? parametre girmeden endpointin hata vermeden çalışması için;
        if start is not None or end is not None:
        #? yani parametre varsa if bloğu çalışsın
        #? parametre yoksa direk return çalışsın
        
            # not_available = Reservation.objects.filter(
            #     end_date__gt=start, end_date__gt=start
            # ).values_list("car_id", flat=True) 
            
            not_available = Reservation.objects.filter(
                condition1 & condition2
            ).values_list("car_id", flat=True) 
            # önce Reservasyonlarrdan müsait olmayan araçları yazılan conditionlara göre filitreledi,
            # daha sonra values_list ile sadece bir field aldı, car_id
            # flat=True ise liste olarak dönmesini sağlıyor,
            # sonuçta not_available olarak, müsait olmyan araçların id'lerinin listesi gelir,  [1,2] gibi bir liste dönüyor.
            print(not_available)
            
            queryset = queryset.exclude(id__in=not_available)
            # artık müsait olmayanları bulduğumuza göre, tamamından exclude ile ayırırsak geriye sadece müsaitler kalır.
        
        return queryset   
    
    #todo, ilave serializer ile;  
    # def get_serializer_class(self):
    #     if self.request.user.is_staff:
    #         return CarSerializer
    #     else:
    #         CarSerializerNotStaff     
    
    
class ReservationMVS(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    
    
    #! task, can see the list of their reservations including past ones

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = super().get_queryset()
        else:
            queryset = super().get_queryset().filter(customer_id= self.request.user.id).filter(end_date__gt=timezone.now())
        print(queryset)
        reserve = ReservationSerializer(queryset[0]).data
        print("reserve : ", reserve)
        # print("car_id : ", reserve.get("car_id"))
        print("car_id : ", reserve["car_id"])
        reserve_car_id = reserve["car_id"]
        car_reserve = Reservation.objects.filter(car_id = reserve_car_id, end_date__gt=timezone.now())
        print(car_reserve)
        return queryset
    



    
"""  django filter kullanımı örneği;
people = Person.objects.filter(age__gt=20, name__contains='John') 
Bu kod, 20'den büyük yaşta ve ismi 'John' olanları döndürecektir.
Django, filter() metodunda birçok kıyaslama operatörü sunmaktadır. Örnek olarak:
exact: esitliği kontrol eder.
iexact: case-insensitive esitliği kontrol eder.
contains: bir string içinde arama yapar.
icontains: case-insensitive bir string içinde arama yapar.
gt: büyüklük karşılaştırması yapar.
gte: büyüklük veya eşitlik karşılaştırması yapar.
lt: küçüklük karşılaştırması yapar.
lte: küçüklük veya eşitlik karşılaştırması yapar.
in: belirli bir liste içinde arama yapar.
    
"""


class ReservationView(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated,)
    
    #! task, can see the list of their reservations including past ones
    #? staff/admin ise bütün rezervasyonları, değilse sadece kendi rezervasyonlarını görsün,
    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return super().get_queryset().filter(customer=self.request.user)


class ReservationDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    # lookup_field = 'id'

    #! task, can update reservations, but can not extend end dates 
    #! if the car is reserved by other customers on selected time.

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        end = serializer.validated_data.get('end_date')
        car = serializer.validated_data.get('car')
        start = instance.start_date
        today = timezone.now().date()
        if Reservation.objects.filter(car=car).exists():
            # a = Reservation.objects.filter(car=car, start_date__gte=today)
            # print(len(a))
            for res in Reservation.objects.filter(car=car, end_date__gte=today):
                if start < res.start_date < end:
                    return Response({'message': 'Car is not available...'})

        return super().update(request, *args, **kwargs)
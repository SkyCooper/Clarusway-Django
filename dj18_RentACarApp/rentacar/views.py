from .serializers import CarSerializer, ReservationSerializer
from .models import Car, Reservation
from rest_framework.viewsets import ModelViewSet
from .permissions import IsStafforReadOnly
from django.db.models import Q
# Create your views here.

class CarMVS(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsStafforReadOnly,)
    
    
    #? availibity sadece staff bilsin, client sadece müsait olanları görsün diye,
    #? tarih aralığını yakalamak için  request.query_params.get() kullanılıyor,
    #? query_params bir dictionary olduğundan key start olan ve end olan değerleri alıyoruz,
    #* http://127.0.0.1:8000/api/car/?start=2023-02-15&end=2023-02-20 böyle bir endpoint yazıyoruz bakmak için,
    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = super().get_queryset()
        else:
            queryset = super().get_queryset().filter(availibity=True)
        start = self.request.query_params.get("start")
        end = self.request.query_params.get("end")
        # print(start, end)
        
        #? available olanlar için bir condition yazıyoruz
        condition1 = Q(start_date__lt=end) #less than
        condition2 = Q(end_date__gt=start) #greater than
        not_available = Reservation.objects.filter(
            condition1 & condition2
        ).values_list("car_id", flat=True) #[1,2] gibi bir dizi dönüyor.
        print(not_available)
        
        queryset = queryset.exclude(id__in=not_available)
        return queryset        
    
    
class ReservationMVS(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    
    
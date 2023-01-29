from rest_framework import serializers
from .models import Car, Reservation

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("id", "plate_number", "brand", "model",
                  "year", "gear", "fuel", "rent_per_day", "availibity")
        
    #! availibity ve plate_number fieldlerini admin görsün, client görmesin diye get_fields override ediyoruz,  
    def get_fields(self):
        fields =super().get_fields()
        request = self.context.get("request")
        
        if request.user and request.user.is_staff:
            fields.pop("availibity")
            fields.pop("plate_number")
        return fields

#todo, ilave serializer ile;    
# Bu method u override etmek yerine staff ve normal userlar için ayrı ayrı serializerlar oluşturulup
# View de get_serializer_class methode u override edilerek user a göre serializerlar seçilebilir.

# class CarSerializerNotStaff(serializers.ModelSerializer):
#     class Meta:
#         model = Car
#         fields = (
#             'id',
#             'brand',
#             'model',
#             'year',
#             'gear',
#             'rent_per_day',
#         )



class ReservationSerializer(serializers.ModelSerializer):
    car = serializers.StringRelatedField()
    car_id = serializers.IntegerField()
    customer = serializers.StringRelatedField()
    reserved_days = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = Reservation
        fields = ("id", "car", "customer", "start_date", "end_date", "reserved_days", "car_id", "total_price")
        
        #? aynı reservasyon database gitmeden uyarı versin diye validators tanımlıyoruz,
        #? queryset, hangi tabloya bakacak
        #? fields,  tablodaki hangi fieldlar uniq olacak,  burada üçü aynı anda,
        #? message, uniq değilse, aynı rezervasyandon varsa ne mesaj verek,
        validators = [
            serializers.UniqueTogetherValidator(
                queryset = Reservation.objects.all(),
                fields = ("customer", "start_date", "end_date"),
                message=("You already have same reservation these dates..")
            )
        ]
    
    #? Reservasyon süresi toplam kaç gün,
    def get_reserved_days(self, obj):
        return obj.end_date.day - obj.start_date.day
    
    #? Rezervasyon toplam ücreti ne kadar,
    def get_total_price(self, obj):
        return obj.car.rent_per_day * (obj.end_date - obj.start_date).days
        # return obj.car.rent_per_day * obj.reserved_days
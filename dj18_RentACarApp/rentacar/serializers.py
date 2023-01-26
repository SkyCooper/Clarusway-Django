from rest_framework import serializers
from .models import Car, Reservation

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("id", "plate_number", "brand", "model",
                  "year", "gear", "fuel", "rent_per_day", "availibity")
        
        
class ReservationSerializer(serializers.ModelSerializer):
    car = serializers.StringRelatedField()
    customer = serializers.StringRelatedField()
    reserved_days = serializers.SerializerMethodField()
    class Meta:
        model = Reservation
        fields = ("id", "car", "customer", "start_date", "end_date", "reserved_days")
        
    def get_reserved_days(self, obj):
        return obj.end_date.day - obj.start_date.day
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
    
class Car(models.Model):
    
    GEAR = (
        ("A", "Automatic"),
        ("M", "Manual"),)

    FUEL = (
        ("D", "Diesel"),
        ("P", "Petrol"),
        ("H", "Hybrid"),
        ("E", "Electric"),
        ("L", "LPG"),)
    
    plate_number = models.CharField(max_length=15, unique=True)
    brand = models.CharField(max_length=15)
    model = models.CharField(max_length=25)
    year = models.SmallIntegerField()
    gear = models.CharField(max_length=1, choices=GEAR)
    fuel = models.CharField(max_length=1, choices=FUEL)
    rent_per_day = models.DecimalField(max_digits=7,
                                            decimal_places=2,
                                            validators=[MinValueValidator(1)])
    availibity = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return f"{self.brand}/{self.model} - {self.plate_number }"
    
class Reservation (models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customers")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="cars")
    start_date = models.DateField()
    end_date = models.DateField()
    
    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"
        
        #! task, can choose a car on the list and reserve that car, but can not reserve more than one car on a selected time period
        #? eğer ikili/üçlü fieldlarda unuiqlik oluşturmak istiyorsak UniqueConstraint kullanıyoruz,
        #? müşteri- aynı tarihler arasında başka araç kiralayamaz bu durumda,
        #? cooper - mercedes - 15 - 18  ilk reservasyon
        #? cooper - mercedes - 18 - 19  olur 
        #? cooper - audi     - 15 - 18  olmaz araç farklı ama müşteri ve tarihler aynı
        #? henry - mercedes  - 15 - 18  olur, müşteri farklı
        #? cooper - audi     - 15 - 18  olmaz çünkü araca bakmıyor,
        constraints = [
            models.UniqueConstraint(
                fields = ["customer", "start_date", "end_date"],
                name="user_rent_date"
            )
        ]
    
    def __str__(self):
        return f"Customer {self.customer} reserved {self.car}"
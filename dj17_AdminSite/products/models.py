from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_in_stock = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
    
    def __str__(self):
        return self.name
    
    #? CustumAdmin içinde yazdığımız metodun aynısını burada yazabiliriz, obj/product yazmaya gerek kalmaz
    # def added_days_ago(self):
    #     fark = timezone.now() - self.create_date
    #     return fark.days
    
    
    #? Custum metod yazabiliriz, obj yazmaya gerek kalmaz
    #? görmek için admin.py'de fields içine eklemek gerekir.
    #? bunun aynısını obj ile admin.py tarafında da yapabiliriz.
    def how_many_reviews(self):
        count = self.reviews.count()
        return count
    
#! ürünlere ait yorumlar tablosu
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    is_released = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"{self.product.name} - {self.review}"
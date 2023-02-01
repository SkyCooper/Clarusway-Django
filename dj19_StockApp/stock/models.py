from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=25)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"

    def __str__(self):
        return self.name
    
    
class Brand(models.Model):
    name = models.CharField(max_length=25)
    image = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.name


    
class Firm(models.Model):
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    image = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Firm"
        verbose_name_plural = "Firms"

    def __str__(self):
        return self.name
    


class Product(models.Model):
    name = models.CharField(max_length=25, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=25)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, max_length=25)
    stock = models.SmallIntegerField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
    


class Purchases(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, max_length=25)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, max_length=25)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, max_length=25)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, max_length=25)
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(1)])
    price_total = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    
    class Meta:
        verbose_name = "Purchases"
        verbose_name_plural = "Purchases"

    def __str__(self):
        return f"{self.product}/{self.brand} - {self.quantity}"
    

class Sales(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, max_length=25)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, max_length=25, related_name="sales")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, max_length=25)
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(1)])
    price_total = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    
    class Meta:
        verbose_name = "Sales"
        verbose_name_plural = "Sales"

        

    def __str__(self):
        return f"{self.product} - {self.quantity}"




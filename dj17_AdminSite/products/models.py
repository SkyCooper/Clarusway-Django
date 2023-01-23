from django.db import models
from django.utils import timezone
#? RichTextField
from ckeditor.fields import RichTextField

#! many-to-many ilişkileri görmek için category model ekledik,
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="category name")
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    # description = models.TextField(blank=True, null=True)
    #? RichTextField
    description = RichTextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_in_stock = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)
    #? bir ürün birden fazla kategori tablosunda olabilir,
    categories = models.ManyToManyField(Category, related_name="products")
    #? image'ler için sonradan eklendi,
    product_img = models.ImageField(null=True, blank=True, default="defaults/clarusway.png", upload_to="product/")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
    
    def __str__(self):
        return self.name
    
    #? Custum Admin içinde (admin.py deki ProductAdmin) yazdığımız metodun aynısını burada yazabiliriz,
    #* obj/product yazmaya gerek kalmaz
    #? burada yorumda, admin.py de aktif,
    # def added_days_ago(self):
    #     fark = timezone.now() - self.create_date
    #     return fark.days
    
    #? kaç tane yorum yapılmış, görmek için;
    #? Custum metod yazabiliriz, obj yazmaya gerek kalmaz
    #? görmek için admin.py'de fields içine eklemek gerekir.
    #? bunun aynısını obj ile admin.py tarafında da yapabiliriz.(orada yorum olarak var,)
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
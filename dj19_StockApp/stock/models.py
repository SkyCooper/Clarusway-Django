from django.db import models
from django.contrib.auth.models import User

#? UpdateCreate modeli aslında diyagramda yok, (abstract örnek olsun diye yaptı)
#? ortak olan fieldlar için abstract Class yapılıp ihtiyaç olan yerde kullanılabilir,
#? mesela her modelde created ve updated fieldları olsaydı,
#? artık Product(models.Model)'den değil Product(UpdateCreate) den abstract edebiliriz.
#? abstract edilenlerde created ve updated fieldları ile sonradan eklenenlerde var artık.
class UpdateCreate(models.Model):
    createds = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=25)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
    
class Brand(models.Model):
    name = models.CharField(max_length=25, unique=True)
    image = models.TextField()
    
    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.name


class Product(UpdateCreate):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="b_products")
    stock = models.PositiveSmallIntegerField(blank=True, default=0)
    #? eksi değer olmasın diye PositiveSmallIntegerField
    
    #* abstract edildiği için bunlarda vardır field olarak
    # createds = models.DateField(auto_now_add=True)
    # updated = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    
class Firm(UpdateCreate):
    name = models.CharField(max_length=25, unique=True)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=200)
    image = models.TextField()
    
    #* abstract edildiği için bunlarda vardır field olarak
    # createds = models.DateField(auto_now_add=True)
    # updated = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Firm"
        verbose_name_plural = "Firms"

    def __str__(self):
        return self.name
    

class Purchases(UpdateCreate):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    firm = models.ForeignKey(Firm, on_delete=models.SET_NULL, null=True, related_name="f_purchases")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name="b_purchases")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="p_purchases")
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    price_total = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
    #?------------- blank=True , null=True ----------------
    # blank=True, serializer ile ilgilidir (frontend'ten datanın gelişi ile), yani boş bırakılabilir,
    # null=True, DB ile ilgilidir, yani boş bırakılabilir ve DB null kayıt edilir,
    #! eğer sadece  blank=True varsa veri boş gelebilir, ama DB kayıt edilmeden önce
    #! bir işlem/hesaplama vs. yapılıp DB boş/null gitmesini önlemek gerekir.

    
    #* abstract edildiği için bunlarda vardır field olarak
    # createds = models.DateField(auto_now_add=True)
    # updated = models.DateField(auto_now=True)
    class Meta:
        verbose_name = "Purchases"
        verbose_name_plural = "Purchases"

    def __str__(self):
        return f"{self.product} - {self.quantity}"
    

class Sales(UpdateCreate):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name="b_sales")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="p_sales")
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    price_total = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
    
    #* abstract edildiği için bunlarda vardır field olarak
    # createds = models.DateField(auto_now_add=True)
    # updated = models.DateField(auto_now=True)
    class Meta:
        verbose_name = "Sales"
        verbose_name_plural = "Sales"

    def __str__(self):
        return f"{self.product} - {self.quantity}"

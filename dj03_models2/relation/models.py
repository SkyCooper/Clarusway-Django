from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
  bio = models.TextField(blank=True)
  image = models.ImageField(upload_to='profile', blank=True, null=True) 
  #? upload_to='profile' => eklenecek resimler, media altında profile diye bir klasör oluşsun 
  #? ve oraya kayıt edilsin demek
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
  #? hangi kullanıcı ile ilişkili buradan belirtiyoruz. User tablosu(modeli) ile OneToOne ilişki kuruldu.
  #? on_delete=models.CASCADE
  
  def __str__(self):
    return self.user.username
    #* bu user ait username görünsün demek
  
class Address(models.Model):
  name = models.CharField(max_length=20)
  address = models.CharField(max_length=150)
  city = models.CharField(max_length=20)
  phone = models.CharField(max_length=20)
  user = models.ForeignKey(User, on_delete=models.CASCADE) #? relations burada belirtiliyor.
  
  def __str__(self):
    return self.name
  
class Product(models.Model):
  name = models.CharField(max_length=100)
  user = models.ManyToManyField(User) #!on_delete burada yok, ManyToMany olduğundan
  
  def __str__(self):
    return self.name
  
'''
on_delete properties:
    # CASCADE -> if primary deleted, delete foreing too.
    # SET_NULL -> if primary deleted, set foreign to NULL. (null=True)
    # SET_DEFAULT -> if primary deleted, set foreing to DEFAULT value. (default='Value')
    # DO_NOTHING -> if primary deleted, do nothing.
    # PROTECT -> if foreign is exist, can not delete primary.
'''

  
'''
on_delete properties: (Profile içinde user'a verildi yukarıda)
    # CASCADE -> if primary deleted, delete foreing too. (user silince ona ait profile/address de sil)
    # SET_NULL -> if primary deleted, set foreign to NULL. (null=True kullanmak gerekiyor) (user silinse bile profile bilgisi kalsın istersek kullanılır ve null atar)
    # SET_DEFAULT -> if primary deleted, set foreing to DEFAULT value. (default='Value') (mesela anynomous verilir default, user silinince anynomous user olarak kalır.)
    # DO_NOTHING -> if primary deleted, do nothing. (birşey yapma, user silinse bile bütün profile bilgisi kalsın demek)
    # PROTECT -> if foreign is exist, can not delete primary. (user'ın silinmesine izin verme, başka tablolara bağlı vs'den dolayı)
'''
#? on_delete properties:
  #* OneToOne
  #* OneToMany  bu ikisinde kullanılır,

  #! ManyToMany bunda kullanımaz,
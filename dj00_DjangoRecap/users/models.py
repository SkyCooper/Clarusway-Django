
#? 1inci yöntem için;
# from django.contrib.auth.models import AbstractUser
# from django.conf import settings
# from datetime import date


#? 2nci yöntem için;
from django.db import models
from django.contrib.auth.models import User

#! Eğer Kullandığımız User tablosu bize yetmez ise ilave yöntemler kullanabiliriz;

#? 1inci yöntem
# User modeli --> class User(AbstractUser): inherit edilerek yapılmış
# Biz de AbstractUser'dan  inherit ederek kendi User modelimizi oluşturabiliriz.
# Buna exdending user table deniyor,

# class MyUser(AbstractUser):
#   username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
#   email = models.EmailField(('email address'), unique = True)
#   native_name = models.CharField(max_length = 5)
#   phone_no = models.CharField(max_length = 10)
#   USERNAME_FIELD = 'email'
#   REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
  
#   def __str__(self):
#       return "{}".format(self.email)

#* base.py içine;
# AUTH_USER_MODEL = "users.MyUser" --> ekle


#? 2nci yöntem
# yeni bir tablo oluşturup, bunu onetoone ile mevcut User tablosuna bağlayarak yapma;
# böylece mevcut User'lara ilave fieldlar ekleyebiliriz.
# Şimdi bu yöntemi kullanıp her bir User'ın Profile bilgilerini tutacağımız bir Profile Tablosu eklicez,

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    avatar = models.ImageField(upload_to="profile_pictures", default="avatar.png")
    # upload_to='student_pictures' => eklenecek resimler, media altında student_pictures diye bir klasöre kayıt edilsin demek
    # default = "avatar.png" , resim eklenmezse media ana klasörü içindeki avatar.png'yi alsın demektir.
    
    # projelerde static'ler db olmaz, başka bir depolama alanında olur
    # https://django-storages.readthedocs.io/en/latest/
    
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
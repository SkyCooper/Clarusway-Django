
#! ***********************************************
#! users klasörünü en baştan yapmak için;
#! ***********************************************

#* rest-auth token kullanmak için;
pip install dj-rest-auth
pip freeze > requirements.txt

#* ekle
INSTALLED_APPS = (
    ...,
    'rest_framework',                   #? yoksa bunu ekle
    'rest_framework.authtoken',         #? yoksa bunu ekle
    ...,
    'dj_rest_auth', #! bunu ekle
)


#* USER (register/login/logout) (dj09)
# Önce yeni bir app oluşturuyoruz (sadece bu işlemleri yapacak)
python manage.py startapp users

#* ekle
INSTALLED_APPS = (
    ...,
    'users',
)

# main -> settings kalsörü  en sonuna ekle,
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

# tekrar migrate yap ve çalıştır.
python manage.py migrate
python manage.py runserver

#* sonuna slash / eklemeyi unutma!!!!
http://127.0.0.1:8000/users/auth/

#* dokuman adresinden demo proje indirilip özelliklerine bakılabilir
https://dj-rest-auth.readthedocs.io/en/latest/demo.html



# Bu app için ilave model oluşturmadan Djangonun User modelinden faydalanıcaz.
# users içinde serializer.py dosyası oluştur.
from rest_framework import serializers
from django.contrib.auth.models import User  # (default user modeli import ediyoruz)
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer

class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators = [UniqueValidator(queryset=User.objects.all())]
        )
    
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password],
        style = {"input_type" : "password"}
    )
    password2 = serializers.CharField(
        write_only = True,
        required = True,
        style = {"input_type" : "password"}
    )
  
#! yukarıdakileri yazmadan sadece aşağıdakini yazarsak User modeli birebir kopyalamış oluruz, biz yukarıdakileri yazarak İnherit aldığımız modeli override ettik, kendimize göre customize yaptık.  

    class Meta:
        model = User
        fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'password',
        'password2']

  #? Yeni oluşturduğumuz password2 ile password aynımı, bunu konrtol etmek için validate metodunu ekliyoruz.
  #? yazılan metodlarda indentation önemli, class Meta ile aynı hizada,
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {'password': 'Password fields didnt match.'}
            )
        return data

  #? ModelSerializer kullanınca create metodu yazmaya gerek yok aslında fakat, User model içinde olmayan bir field 
  #? (password2) kullandığımız için creat metodunu override etmek gerekli;
  
    def create(self, validated_data): # best practise validated_data yazılır.
        validated_data.pop('password2') # password2 create için gerekli olmadığından dictten çıkardık
        password = validated_data.pop('password') # password sonradan set etmek için dictten çıkardık ve değikene atadık.
        user = User.objects.create(**validated_data) # unpack yapıldı, username=validate_data['username], email = va.......
        # validated_data içinde artık password ve password2 yok, onu kullanarak yeni bir user create edildi.
        user.set_password(password) 
        # yukarıda değişkene atanan password, create edilen user'a atandı,  encrypte olarak db ye kaydedildi.
        user.save()
        # passwor eklenmiş yeni user save edildi.
        return user

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email")
    
    
class CustomTokenSerializer(TokenSerializer):
    user = UserTokenSerializer(read_only = True)
    
    class Meta(TokenSerializer.Meta):
        fields = ("key", "user")


# Daha sonra view ekliyoruz.
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
  
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.get(user=user)
        data = serializer.data
        data["key"] = token.key
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


# endpintleri belirtmek gerekli;
# önce main içinden urls.py'dan yönlendirme yapıyoruz.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")), #! bunu ekle,
]

# sonra users içine urls.py dosyası oluşturuyoruz.
from django.urls import path,include
from .views import RegisterView

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path("register/", RegisterView.as_view())
]



#* signal kullanarak token oluşturma,
#* signal'in görevi = başka bir olayı trgger etme / tetikleme,
  #? register olunca token oluşması signal ile yapıldığında models.py içinde yazılması lazım ama 
  #? kalabalık olmasın diye signals.py dosyası oluşturulup orada yapmak daha uygun
  
#* users app içine signal.py dosyası oluştur.

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


#! yeni bir user oluşturulduğunda ona token oluşturması için receiver dekoratoru ile yazılan metod;
#! bu bize register olduktan sonra tekrar login sayfasına gitmeden login olmamızı sağlıyor.

#? post_save , yani işlem/olay  bittikten sonra, yani user create edildikten sonra
#? sender=User, User tablosundan yeni user create edilince singnal gönder ve bunu reciver dekaratoru ile yakala

@receiver(post_save, sender=User)
def create_Token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
#? model içine yazmayıp signals.py olarak ayrı bir dosyada yazdığımız için apps.py içine eklemek gerekli
#? apps.py otomatik çalışan bir dosyadır.   ->  signals.py dosyasını çağırdı. 
#? apps.py dosya içeriği aşağıdaki gibi olmalı. 

from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    
    def ready(self) -> None:
        import users.signals
        
#! ***********************************************
#! users klasörünü içine Profile model eklemek için;
#! ***********************************************

# models.py içine;
from django.db import models
from django.contrib.auth.models import User

#? açıklama
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



# serializers.py içine;
#? ilave porfile serializer
class ProfileSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField(required=False)
    
    class Meta:
        model = Profile
        fields = ("id","user","user_id", "display_name","avatar", "bio")
        
#! buradaki ProfileSerializer'ın kullanıldığı view (ProfileUpdateView)
#! RetrieveUpdateAPIView'dan inherit edildiği için create metodu değil update metodu override edilmeli,        
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.user_id = self.context['request'].user.id
        instance.save()
        return instance



# view.py içine;
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.generics import RetrieveUpdateAPIView
from .permissions import IsOwnerOrStaff
from rest_framework.permissions import IsAuthenticated

#! profile için;
class ProfileUpdateView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsOwnerOrStaff, IsAuthenticated]




# urls.py içine;
#? profile için;
from .views import ProfileUpdateView

urlpatterns = [ path("profile/<int:pk>/", ProfileUpdateView.as_view()), ] #ekle



# signals.py içine;
from .models import Profile

#? bir kullanıcı register olduğunda ona Profile otomatik create edilmesi için;  
@receiver(post_save, sender=User)
def create_Profile(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.create(user=instance)






#! ***********************************************
#! users klasörünü başka bir projeden kopyalarsak;
#! ***********************************************

#* rest-auth token kullanmak için;
pip install dj-rest-auth
pip freeze > requirements.txt

#* python setup.py egg_info did not run successfully.
# eğer böyle bir hata alırsan,
pip install --upgrade setuptools
# sonra tekrar dj-rest-auth yükle,

#* ekle
INSTALLED_APPS = (
    ...,
    'rest_framework',                   #? yoksa bunu ekle
    'rest_framework.authtoken',         #? yoksa bunu ekle
    ...,
    'dj_rest_auth', #! bunu ekle
)

#* ekle
INSTALLED_APPS = (
    ...,
    'users',
)

# main -> settings kalsörü  en sonuna ekle,
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

# migrate yap ve çalıştır.
python manage.py migrate
python manage.py runserver


# eğer pillow kurmak gerekirse 
#* IMAGE (resim) işleme eklentisi kurma 
pip install pillow
pip freeze > requirements.txt
# kurulum yapılan her paketten sonra güncel olarak txt içine işlemek için yukarıdaki komutu çalıştır.

# main settings içine 
STATIC_URL = 'static/' ---> bunun altına ekle;
1-
MEDIA_URL = 'media/'
2-
MEDIA_ROOT = BASE_DIR / 'media/'

# media_url -> hangi urlyi kullanacaksın
# media_root -> hangi klasöre yüklemek istersin.
# ilk resim eklendikten sonra media isimli bir klasör oluşur ve eklenen resim oraya kayıt edilir.

# https://docs.djangoproject.com/en/4.1/howto/static-files/
# bu adresten nasıl yapılacağına bak, import vs. nasıl yapılacak...

# main urls içine aşağıdaki importları yaz ve urlpatterns ekle.
3-
from django.conf import settings
from django.conf.urls.static import static

urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# tekrar migrate yap ve çalıştır.
python manage.py migrate
python manage.py runserver


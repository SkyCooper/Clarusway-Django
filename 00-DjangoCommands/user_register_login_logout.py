
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
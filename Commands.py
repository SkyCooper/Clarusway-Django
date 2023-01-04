# (LMS teki kurulum vido linki =>  How to Install and Use Django 
#? https://youtu.be/osKPG2ripmw 

# ORM-> python ile yazılan sorgu kodlarını arka plandaki database için SQL formatına çevirir.

#* Check the versions of Python and pip
python --version
pip --version

#! SIFIRDAN BİR PROJE BAŞLATMAK İÇİN;
#* Install virtual environment
python -m venv env 
# (bunu yapmamızın sebebi sistemlerin, paketlerin versiyonları değişse bile
# daha sonradan hata vermeden kullanılabilsin diye global'de değil virtual'da çalışmak lazım.)
# (buradaki env => bestpractice dosya ismi)

#* activate virtual environment
bash            source env/Scripts/Activate
# Powershell    => .\env\Scripts\activate
# linux/mac     => source env/bin/activate 

# deactivate virtual environment
deactivate

# activate esnasında hata olursa bu komutu kullan;
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted

#* django kurumak için;
pip install django

#* django'nun API servisi gibi çalışması için bir micro-framework olan;
#* restframework kurmak için;
pip install djangorestframework
# sadece yukarıdaki komutu çalıştırsak önce django, sonra restframework kurar.
# daha sonra main/settings.py INSTALLED_APPS içine  'rest_framework', ekle
# tırnak içinde ve mutlaka sonunda virgül ile,

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #thirdparty apps
    'rest_framework',
  
]

#* pip update için;
pip install --upgrade pip
python -m --pip install --upgrade pip


#* gitignore dosyası oluşturma;
# ana dizine .gitignore isminde dosya oluştur.
# https://www.toptal.com/developers/gitignore/api/django adresinden Template olarak al
# env'den farklı bir isim verdiysen gitignore içine ilgili bölüme dosya ismini ekle..

# Environments
# .env
# .venv
# env/
# venv/
# ENV/
# env.bak/
# venv.bak/
#? .cooper (mesela böyle bir isim verdiysen .gitignore içindeki bölüme ekle)

#* yeni bir proje başlatmak için;
django-admin startproject main .
# main klasörü ekle (bestpractice), nokta(.) kullan, iç içe olmaması için

#* kurulan paketleri görmek için;
pip freeze veya 
pip list

#* kurulan paketleri txt dosyasına kayıt etmek için;
pip freeze > requirements.txt
# yüklü paketleri txt dosyasına kaydettik bunu yapmamızın sebebi
# projeyi sunduğumuzda kullandığımız paketleri göstermesi için

#! BİR REPODAN PULL EDİLEN VEYA KOPYALANAN BİR PROJE BAŞLATMAK İÇİN;
#* Install virtual environment (env yoksa)
python -m venv env

#* activate virtual environment
bash            source env/Scripts/Activate
# Powershell    => .\env\Scripts\activate
# linux/mac     => source env/bin/activate 

#* projeyi ayağa kaldırmak için
pip install -r requirements.txt


#! PROJE BAŞLATMAK İÇİN;
#* server çalıştır.
python manage.py runserver (default port 8000)
python manage.py runserver 8080 (port numarasını değiştirme )

#* terminaldeki migrate uyarılarını düzeltmek için,
# You have 18 unapplied migration(s). bu uyarı default olarak djangonun oluşturduğu app'lerden kaynaklanıyor.
python manage.py migrate

#* server durdur.
ctrl + c

# terminalden proje başlattıktan sonra artık terminale konut yazılamaz,
# bunun için ya projeyi durdur, ya da yeni bir terminal aç
# eğer yeni bir termimale geçersen env aktif mi? kontrol et değilse aktif et.
source env/Scripts/Activate


#* Admin olarak LOGIN olmak için;
python manage.py createsuperuser

# fakat bu kod çalışmadan migrate hatası verebilir, eğer önceden migrate yapılmamış ise;
python manage.py migrate 	
# bu komuttan sonra tekrar yukarıdaki komutu çalıştır.

# Username : ( admin yazılabilir bestpractice )
# Email adress: (Boş bırakmak için ENTER ile geçilebilir.)
# Password: **********
# Password (again): ********* (yazarken görünmez)
# Superuser created successfully.

# daha sonradan güvenli şekilde bakmak için
#? .env dosyası oluşturulup username ve Password bilgisi oraya kayıt edilebilir

# http://127.0.0.1:8000/admin/ bu adrese username ve şifre ile girildiğinde
# Djangonun default oluşturduğu Groups ve Users tabloları görünür.

#! APPLICATION OLUŞTURMAK İÇİN;
#todo, 1- önce yeni bir app oluştur,
#todo, 2- bu app içinde models.py içinde model oluştur,
#todo, 3- serializer.py dosyasını ekle ve bu modele ait bir serializer yaz, 
#todo, 4- oluşturulan model ve serializer kullanarak view.py içinde view oluştur,
#todo, 5- urls.py dosyasını ekle ve bu view için bir url (endpoint) yaz.

#todo, 1-yeni bir app(klasör) oluşturma;
"""

# manage.py ile aynı dizinde olduğundan emin ol
python manage.py startapp nameofyourproject (fscohort vs.)
veya; django-admin startapp nameofyourproject (fscohort vs.)
# aslında yukarıdaki komut da aynı işemi yapar.
# fakat manage.py dosyası oluştuğundan best practise birinci komutu kullanmak.

# bunu yaptıktan sonra proje dizinine(main) gidip;
#* settings.py içinde INSTALLED_APPS listesi içine proje ismini eklememiz gerekiyor

# eklerken karışmaması için önce #myapps gibi bir yorum satırı ekleyip
# sonra tırnak içinde app ismi ve sonrasında virgül koymak okunurluğu arttırır.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #my apps
    'nameofyourproject',
    'fscohort',
    'dscohort',
    'awscohort',
    
    #thirdparty apps
    'rest_framework',
  
]
"""

#todo, 2-Model oluşturma;
"""
from django.db import models

# models.py'deki her class database'de bir tablo'dur
# classlardaki her instance tablonun bir sütünudur..

class Classname(models.Model):
  pass # hiçbirşey yazılmayacaksa pass yazılır. Format bu

# models.py dosyası içerisine bir model oluşturduktan sonra ve
# modellerde işlem/değişiklik yapınca sırasıyla bu komutları çalıştır;

1 - python manage.py makemigrations nameofyourproject (fscohort vs.)
# Django'ya modellerinizde bazı değişiklikler yaptığınızı
# ve değişikliklerin depolanmasını istediğinizi söylüyorsunuz.

2- python manage.py migrate 
# Migrate komutu, uygulanmamış değişiklikleri alır ve bunları veritabanınızda çalıştırır
# modellerinizde yaptığınız değişiklikleri veritabanındaki şema ile senkronize eder.

#* DATABASE'de değişiklik yapılınca bu 2 komut mutlaka tekrar çelıştırılır.

# http://127.0.0.1:8000/admin/ daha sonra bu adresten login ekranına gidilir.
# burada oluşturulan model (tablo) görünmez,
# bunun için oluşturulun app içindeki admin.py içerisine model (tablo) import edilmeli;

from django.contrib import admin
from .models import ModelName
# Register your models here.

admin.site.register(ModelName)

# http://127.0.0.1:8000/admin/ tekrardan bu adrese gidilince Groups ve Users tabloları ile
# bizim oluşturduğumuz model(tablo) artık burada görünür.
"""

#todo, 3-Serializer oluşturma;
"""
# önce app(klasör) içinde serializer.py isimli dosya oluştur.
# kullanılacak model ve serializers importunu yap
from rest_framework import serializers
from .models import Classname

class NameSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Todo
    fields = ["id", "task", "description", "priority", "is_done", "created_date"]
    # fields = '__all__'  (böyle de kullanılabilir.)
"""

#todo, 4-View oluşturma;
"""
# app içindeki views.py dosyası içinde kullanıma göre
# FBV (Function Based View)
# CBV (Class Based View) importları ile kullanıcak model ve serializer'ları import et

from rest_framework.response import Response

#? FUNCTION BASED VIEW
from rest_framework.decorators import api_view
from rest_framework import status

#? CLASS BASED VIEW
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

#? my imports,
from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer

# best practise yukarıdaki gibi ayırmak okunurluğu arttırır. 
# bundan sonra hangi metod ile yazılacaksa view oluştur. 
"""

#todo, 5-Url oluşturma;
"""
# oluşturulan view için bir url (endpoint) yazmak için önce main urls.py içinden yönlendirme yapmak gerekli
# bunun için include ile app içindeki url dosyasına yönlendirme yapılır. ('tırnak içinde yazılır')

from django.contrib import admin
from django.urls import path, include # (include ile app içindeki url yönlendirme yapılır.) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("name/", include("appname.urls")),
]

# daha sonra app içinde olmayan urls.py dosyası oluşturulur.
# path ve kullanılacak view'ler import edilir.
# Aşağıdaki örnekte hem FBV, hem de CBV için çeşitli örnekler verilmiştir,
# bunlardan sadece kullanılacak olan import edilir.
# eğer CBV için bir url oluşturulacaksa FBV'den farklı olarak sonuna as_views() yazılması gerekir.
# CBV olarak, 

from django.urls import path
from .views import (
    home,
    
    #! function views
    students_list,
    student_create,
    student_detail,
    student_update,
    student_delete,
    student_api,
    student_api_get_update_delete
    
    #! class views
    #* APIVIEW
    StudentListCreate,
    StudentDetail,
    
    #* GENERIC APIVIEW  -  MIXINS
    StudentGAV,
    StudentDetailGAV,
    
    #* CONCRETE VIEWS
    StudentCV,
    StudentDetailCV,
    
    #* VIEWSETS
    StudentMVS,
    PathMVS
)

#? VIEWSETS için router kurmak ZORUNLU,
router = routers.DefaultRouter() #? router isimli bir instance oluşturduk.
router.register("student", StudentMVS) #? buradaki student prefix, yani url'ye onun yazılması gerekiyor.

urlpatterns = [
    path("", home),
    
    #! function views
    # import edilen herbir view için bir endpoit oluşturulur,
    
    path("student-list/", students_list, name='list'),
    path("student-create/", student_create, name='create'),
    
    #* id ile ulaşılması gerekenler için url sonuna <int:pk> ifadesi eklenir.
    
    path("student-detail/<int:pk>/", student_detail, name='detail'),
    path("student-update/<int:pk>/", student_update, name='update'),
    path("student-delete/<int:pk>/", student_delete, name='delete'),

    
    #! class views
    #? FBV den farkı, sonuna as_views() yazılması
    #* APIVIEW
    path('student', StudentListCreate.as_view()),
    path('student/<int:pk>', StudentDetail.as_view()),
    
    #* GENERIC APIVIEW  -  MIXINS
    path('student', StudentGAV.as_view()),
    path('student/<int:pk>', StudentDetailGAV.as_view()),
    
    #* CONCRETE VIEWS
    path('student', StudentCV.as_view()),
    path('student/<int:pk>', StudentDetailCV.as_view()),
    
    #* VIEWSETS
    #? include ile kullanılıyor ve router'a yönlendirme yapılıyor.
    path('', include(router.urls)), #(bunun yerine aşağıdaki kullanımda görülebilir.)
]

#* böyle de kullanılıyor, karşımıza çıkabilir.
# path('', include(router.urls)), bunu listeden silip altına;
# urlpatterns += router.urls , yazarsak da çalışır.
"""





#* IMAGE (resim) işleme eklentisi kurma 
pip install pillow
pip freeze > requirements.txt
# kurulum yapılan her paketten sonra güncel olarak txt içine işlemek için yukarıdaki komutu çalıştır.

# main settings içine 
STATIC_URL = 'static/' altına ekle;
1-
MEDIA_URL = 'media/'
2-
MEDIA_ROOT = BASE_DIR / 'media/'

# media_url -> hangi urlyi kullanacaksın
# media_root -> hangi klasöre yüklemek istersin.
# ilk resim eklendikten sonra media isimli bir klasör oluşur ve eklenen resim oaraya kayıt edilir.

# https://docs.djangoproject.com/en/4.1/howto/static-files/
# bu adresten nasıl yapılacağına bak, import vs. nasıl yapılacak...

# main urls içine aşağıdaki importları yaz ve urlpatterns ekle.
3-
from django.conf import settings
from django.conf.urls.static import static

urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


-- USER 
--djangonun admin panelde otomatik oluşturduğu "Users" tablosuna(modeline) ulaşmak için;
models.py içine;
from django.contrib.auth.models import User => ile import ediyoruz.

--USER model olarak kullanmak için models içine;
from django.contrib.auth.models import User import et



#* SECRET_KEY gizlemek için eklenecek paket;
pip install python-decouple
pip freeze > requirements.txt
# kurulum yapılan her paketten sonra güncel olarak txt içine işlemek için yukarıdaki komutu çalıştır.

# ana dizine manage.py ile aynı hizada .env dosyası oluştur.
# main/settings.py içine;
from decouple import config => bunu import et 
SECRET_KEY = config("SECRET_KEY") => bu hale getir.

# yeni oluşturulan .env dosyası içine boşluksuz ve tırnaksız olarak key yaz.
# burada önemli config("SECRET_KEY") içine yazılan ile .env içine yazılanın aynı olması lazım
SECRET_KEY=xoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxo
# https://djecrety.ir/ adresinden random key üretilebilir.



#* FAKER için  (dj-08)
pip install Faker
pip freeze > requirements.txt
# kurulum yapılan her paketten sonra güncel olarak txt içine işlemek için yukarıdaki komutu çalıştır.

# faker.py isimli dosya oluştur ve içine fake veri üretecek bir fonksiyon yaz.
# daha sonra terminalden shell'i çalıştırıp, app içineki faker dosyasından veri üretecek fonksiyonu import et
python manage.py shell
from nameofapp.faker import run

# fonksiyonu ismini yazarak çalışmasını sağla ve sonra shell'den çık
run()
exit()



--PAGINATION İÇİN; (dj-08)
settings en sonuna;

hangisini kullanacaksan o kalsın diğer ikili grupları sil...
REST_FRAMEWORK = {
     'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 30,
    
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 30,
    
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.CursorPagination',
    'PAGE_SIZE': 30,
}

custimize etmek için pagination.py ekle;

yapılan paginationı views içine import et,
from .pagination import * (hepsini ekle demek)

views.py içindeki view altına;
pagination_class = CustomPageNumberPagination
(hangisini kullanacaksan adını yaz)

---FİLTER/SEARCH için; (dj-08)

pip install django-filter
pip freeze > requirements.txt

'django_filters',  --> ekle settings içine

settings sonuna ekle;
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}


import et;
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


views.py içindeki view altına;
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["id", "first_name", "last_name"]
    search_fields = ["first_name", "last_name"]
    search_fields=['^first_name']  #baş harfine göre arama yapmak için,
    ordering_fields = ['first_name','last_name']  #* filter boxta hangi seçenekler çıksın istiyorsanız onu yazıyorsunuz
    ordering = ['last_name']  #* default olarak ilk açıldığında buraya yazdığımıza göre sıralıyor


--PERMISSIOIN / AUTHENTICATION  (dj09)
1- BASIC Authotantıcatıon;
settings içine;
REST_FRAMEWORK = { 'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.BasicAuthentication' ] }

Authotantıcatıon yapıldı, sonra permission vermek gerekiyor.
from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser  ---> import et view içine,
viewe ekle ..
permission_classes = [IsAuthenticated] (giriş yapan herkes CRUD yapabilir) 
permission_classes = [IsAdminUser] (sadece admin olan) CRUD yapabilir
permission_classes = [IsAuthenticatedOrReadOnly] Authenticate olan (yani giriş yapan) herşeyi yapar, olmayan sadece GET(read) yapar.

Postmende Basic Authentication işlemlerinde, Headers altında Authorazation (KEY) karşısında --> Bacic xoxoxoxoxx (VALUE) yazıyor. Buradaki xoxoxox giriş yapılan username ve password bilgilerinin Base64 ile şifrelenmiş halidir. 
Bunu okumak için kopyalayıp base64decode gibi sitelere yapıştırırsak username ve password görünür.
Bundan dolayı GÜVENSİZdir.

2- TOKEN Authentication; (Güvenliği arttırmak için tercih ediliyor.)
Üretilen token kullanıcı aktifken var, logout olunca siliniyor, tekrardan kullanılmıyor.
'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication' ]
'rest_framework.authtoken', --> INSTALLED_APPS içine ekle. BU db kullanıcıyı ve ona ait Key tutan bir tablo oluşturuyor,
python manage.py migrate --> çalıştır. (db değişiklik yaptığı için)
python manage.py runserver

Artık admin panelden Tokens tablosu oluştu, oradan kullanıcı için manuel olarak token ekle.
permission_classes = [IsAdminUser] viewde bunu aktif et

postmende Authorazation --> No Auth;
Headers --> Authorazation (Key olarak) bölüm ekle --> karşısına  Token vhfosdbvodjfboıdjboıdjboıj YAZ.
Token bir Authorazation yöntemi, daha sonra Permission durumuna göre izin verilen işlemleri yapabilir, Yani her Token sahibi herşeyi yapamaz, IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly vs. durumuna göre ne kadar izni varsa ona göre işlem yapabilir.


--USER (register/login/logout) (dj09)
Bunun için yeni bir app oluşturuyoruz (sadece bu işlemleri yapacak)
python manage.py startapp user
'user', --> INSTALLED_APPS içine ekle,
Bu app için ilave model oluşturmadan Djangonun User modelinden faydalanıcaz.

user içinde serializer.py dosyası oluştur.
from rest_framework import serializers
from django.contrib.auth.models import User  # (default user modeli import ediyoruz)
from rest_framework.validators import UniqueValidator

class RegisterSerializer(serializers.ModelSerializer): (bir serializer tanımlıyoruz.)
    username = 
    password = 
    password2 =
  
#! yukarıdakileri yazmadan sadece aşağıdakini yazarsak User modeli birebir kopyalamış oluruz, biz yukarıdakileri yazarak İnherit aldığımız modeli override ettik, kendimize göre customize yaptık.  

  class Meta:
    model= User
    fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'password2')

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

--Daha sonra view ekliyoruz.
önce user modeli import ediyoruz,
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token

class RegisterView(CreateAPIView):
  queryset = User.objects.all()
  serializer_class = RegisterSerializer
  
  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    token = Token.objects.create(user_id=response.data['id'])
    response.data['token'] = token.key
    print(response.data)
    return response

--daha sonra urls.py içinde endpintleri belirtmek gerekli;
önce main içinden yönlendirme yapıyoruz.
path("user/", include("user.urls")),

--sonra user içine urls.py dosyası oluşturuyoruz.
from django.urls import path
from .views import RegisterView

from rest_framework.authtoken import views

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path('login/', views.obtain_auth_token),
]

--CORS-HEADERS;
pip install django-cors-headers
https://github.com/adamchainz/django-cors-headers (README bak)

settings içine;

INSTALLED_APPS = [ "corsheaders",  içine ekle, 

MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware", (bu default var, üzerine ekle)

CORS_ALLOW_ALL_ORIGINS = True  --> ekle en sona

CORS_ALLOW_METHODS = [  
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
] (izin verilen metodları ekle)


#! #########################################
#! PostgreSQL - Swagger - Debug Toolbar ekleme
#! -----------------------------------------


#* PostgreSQL setup için  (dj-11)
pip install psycopg2
pip freeze > requirements.txt


#* Swagger için  (dj-11)
pip install drf-yasg
pip freeze > requirements.txt

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #thirdparty apps
    'rest_framework',
    'drf_yasg',  #! buraya ekle,
  
]

# main.urls dosyasına aşağıdakinin aynısını kopyala yapıştır.
from django.contrib import admin
from django.urls import path, include

from django.contrib import admin 
from django.urls import path 
 
# Three modules for swagger:
from rest_framework import permissions 
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi 
 
schema_view = get_schema_view(
    openapi.Info(
    title="Flight Reservation API", 
    default_version="v1",
    description="Flight Reservation API project provides flight and reservation info",
    terms_of_service="#", 
    contact=openapi.Contact(email="rafe@clarusway.com"), # Change e-mail on this line!
    license=openapi.License(name="BSD License"),),
    public=True, 
    permission_classes=[permissions.AllowAny],
    )
urlpatterns = [
    path("admin/", admin.site.urls),
    # Url paths for swagger:
    path("swagger(<format>\.json|\.yaml)",schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0),name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

#! daha sonra mutlaka migrate komutunu çalıştır.
py manage.py migrate


#* Debug Toolbar için  (dj-11)
pip install django-debug-toolbar
pip freeze > requirements.txt

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #thirdparty apps
    'rest_framework',
    'drf_yasg',
    'debug_toolbar',  #! buraya ekle,
  
]

# main urls.py içindeki urlpatterns içine aşağıdaki path ekle,
# from django.urls import include, eklenmemiş ise #* include import et

from django.urls import path, include
urlpatterns = [
    # path("admin/", admin.site.urls),
    # # Url paths for swagger:
    # path("swagger(<format>\.json|\.yaml)",schema_view.without_ui(cache_timeout=0), name="schema-json"),
    # path("swagger/", schema_view.with_ui("swagger", cache_timeout=0),name="schema-swagger-ui"),
    # path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path('__debug__/', include('debug_toolbar.urls')), #! buraya ekle, zaten yukarıdakiler vardı.
]

# setting.py içindeki MIDDLEWARE #! en üstüne ekle

MIDDLEWARE = [
'debug_toolbar.middleware.DebugToolbarMiddleware', 
# ...
]

# setting.py içine ekle, yeri önemli değil en sona eklenebilir.
INTERNAL_IPS = [ 
    "127.0.0.1", 
]

#* bütün işlemler tamamlandıktan sonra superuser oluştur ve projeyi çalıştır.
py manage.py createsuperuser
py manage.py runserver

1-admin/
2-swagger(<format>\.json|\.yaml) [name='schema-json']
3-swagger/ [name='schema-swagger-ui']
4-redoc/ [name='schema-redoc']
5-__debug__/

#* yukarıdaki url'ler ve sağ tarafta Debug-toolbar olacak şeklilde gelmesi gerekiyor.



#! #########################################
#! ŞİMDİ YAPILMIŞ BİR PROJENİN AYRILMASI/PARÇALANMASI NASIL YAPILIR
#! -----------------------------------------

#* Seperate Dev and Prod Settings
1- main klasörü içinde settings isminde yeni bir klasör oluştur.
2- bu yeni klasör içinde 4 tane yeni dosya oluştur, 
  - __ini__.py        #* python dosyası olduğunu belirtmek için
  - dev.py            #* development/geliştirme ortamındaki ayarlar için
  - prod.py           #* product/ürün ortamındaki ayarlar için
  - base.py           #* genel/global ayarları kayıt etmek için
  

#* __init__.py dosyası içine;
from .base import *

env_name = config("ENV_NAME")

if env_name == "prod":
  from .prod import *
  
elif env_name == "dev":
  from .dev import *

  
#* dev.py dosyası içine;
from .base import *

THIRD_PARTY_APPS = ["debug_toolbar"]

DEBUG = config("DEBUG")

INSTALLED_APPS += THIRD_PARTY_APPS

THIRD_PARTY_MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"]

MIDDLEWARE += THIRD_PARTY_MIDDLEWARE

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        }
}

INTERNAL_IPS = [
    "127.0.0.1",
    ]


#* prod.py dosyası içine;
from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("SQL_DATABASE"),
        "USER": config("SQL_USER"),
        "PASSWORD": config("SQL_PASSWORD"),
        "HOST": config("SQL_HOST"),
        "PORT": config("SQL_PORT"),
        "ATOMIC_REQUESTS": True,
        }
    }


#* base.py dosyası içine;
"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #? my apps
    
    #? trirdpart apps
    'rest_framework',
    'drf_yasg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

#? for images
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = { 
    "version": 1, 
    # is set to True then all loggers from the default configuration will be disabled. 
    "disable_existing_loggers": True, 
    # Formatters describe the exact format of that text of a log record.  
    "formatters": { 
        "standard": { 
            "format": "[%(levelname)s] %(asctime)s %(name)s: %(message)s" 
        }, 
        'verbose': { 
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}', 
            'style': '{', 
        }, 
        'simple': { 
            'format': '{levelname} {message}', 
            'style': '{', 
        }, 
    }, 
    # The handler is the engine that determines what happens to each message in a logger. 
    # It describes a particular logging behavior, such as writing a message to the screen,  
    # to a file, or to a network socket. 
    "handlers": { 
        "console": { 
            "class": "logging.StreamHandler", 
            "formatter": "standard", 
            "level": "INFO", 
            "stream": "ext://sys.stdout", 
            }, 
        'file': { 
            'class': 'logging.FileHandler', 
            "formatter": "verbose", 
            'filename': './debug.log', 
            'level': 'INFO', 
        }, 
    }, 
    # A logger is the entry point into the logging system. 
    "loggers": { 
        "django": { 
            "handlers": ["console", 'file'], 
            # log level describes the severity of the messages that the logger will handle.  
            "level": config("DJANGO_LOG_LEVEL"), 
            'propagate': True, 
            # If False, this means that log messages written to django.request  
            # will not be handled by the django logger. 
        }, 
    }, 
}


#! pgAdmin uygulamasını aç ve şifreni yazarak giriş yap
#! daha sonra Database üzerine sağ tıklayıp --> create --> database
#! Database ismini yaz, Owner postgres olarak kalacak, başka birşey eklemeden SAVE et.



#! pgAdmin uygulamasından Database oluşturup,
#! settings klasörü içine eklenen 4 yeni dosya içeriği yukarıdaki gibi düzenlendikten sonra;
#* .env dosyası içerisine; aşağıdaki kodları kopyala/yapıştır, (yorumlar silinebilir.)

#* base.py
SECRET_KEY=xwyt@lpf1obsnhwbd30g7z(kp7&*4hdyriv%%a0n4@0$59x
DJANGO_LOG_LEVEL=INFO
#? hangi log kayıtlarını tutacak? INFO = herşey
#? DEBUG, INFO, WARNING, ERROR, CRITICAL

#* __init__.py
ENV_NAME=dev
#? PostgreSQL çalışır
# ENV_NAME=dev
#? SQLite çalışır

#* dev.py
DEBUG=True

#* prod.py
SQL_DATABASE=flight
#? pgAdmin'de oluşturduğumuz database adı
SQL_USER=postgres
#? pgAdmin deki kullanıcı adı (değiştirme)
SQL_PASSWORD=*********
#? pgAdmin'e girdiğimiz şifre
SQL_HOST=localhost
#? burası aynı kalacak (localhost)
SQL_PORT=5432
#? pgAdmindeki default port. eğer değiştirmediysek 5432 kalacak


#! artık main içindeki setting.py dosyasını sil
#* bütün işlemler tamamlandıktan sonra migrate yap, superuser oluştur ve projeyi çalıştır.
py manage.py migrate
py manage.py createsuperuser (daha önceden yapmadıysan)
py manage.py runserver

1-admin/
2-swagger(<format>\.json|\.yaml) [name='schema-json']
3-swagger/ [name='schema-swagger-ui']
4-redoc/ [name='schema-redoc']
5-__debug__/

#* yukarıdaki url'ler ve sağ tarafta Debug-toolbar olacak şeklilde gelmesi gerekiyor.

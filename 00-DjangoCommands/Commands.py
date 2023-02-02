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
# asgiref==3.6.0
# Django==4.1.6
# djangorestframework==3.14.0
# pytz==2022.7.1
pip list  (görünümü daha okunaklı)
# Package             Version
# ------------------- --------
# asgiref             3.6.0
# Django              4.1.6
# djangorestframework 3.14.0

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
# ilk resim eklendikten sonra media isimli bir klasör oluşur ve eklenen resim oaraya kayıt edilir.

# https://docs.djangoproject.com/en/4.1/howto/static-files/
# bu adresten nasıl yapılacağına bak, import vs. nasıl yapılacak...

# main urls içine aşağıdaki importları yaz ve urlpatterns ekle.
3-
from django.conf import settings
from django.conf.urls.static import static

urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#*  USER modelini kullanmak için; 
# djangonun admin panelde otomatik oluşturduğu "Users" tablosuna(modeline) ulaşmak için;
# models.py içine;
from django.contrib.auth.models import User

# daha sonra kullanmak istediğin yerde;
profile = models.Foreignkey(User, on_delete=models.CASCADE) # gibi



#* SECRET_KEY gizlemek için DECOUPLE ekleme;
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
# fake datalar hazırlanan formata göre üretildi, migrate yapmaya gerek yok
python manage.py runserver
# artık admin panelde ve ilgili endpoint'de datalar görünür.


#* CORS-HEADERS
pip install django-cors-headers
# https://github.com/adamchainz/django-cors-headers (README bak)

# settings içine ekle;
INSTALLED_APPS = [ "corsheaders", ]

MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware", #!(bu default var, üzerine ekle)
]

# ekle en sona
CORS_ALLOW_ALL_ORIGINS = True

# izin verilen metodları ekle
CORS_ALLOW_METHODS = [  
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
] 


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








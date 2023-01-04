
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
# fakat şu anda main klasörü yok, oluşturunca eklenecek


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

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #thirdparty apps
    'rest_framework', #! buraya ekle
]

#* kurulan paketleri görmek için;
pip freeze veya 
pip list

#* kurulan paketleri txt dosyasına kayıt etmek için;
pip freeze > requirements.txt
# yüklü paketleri txt dosyasına kaydettik bunu yapmamızın sebebi
# projeyi sunduğumuzda kullandığımız paketleri göstermesi için

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
SECRET_KEY=xwyt@lpf1obsnhwbd30g7z(kp7&*4hdyriv%%a0n4@0$59x
# https://djecrety.ir/ adresinden random key üretilebilir.


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

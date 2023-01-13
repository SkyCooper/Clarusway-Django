# Pyton anywhere deployment, 11.01.2023
# LMS ders linki : https://lms.clarusway.com/mod/page/view.php?id=38465

# https://www.pythonanywhere.com adresinden register ol / üye girişi yap,

Dashboard sekmesinde iken ,
# New Console --> $Bash
# bunu yeni sekmede aç.

# Github reposundan deploy edilecek projenin kodunu kopyala
# açılan Bash Console linux terminaline klonla,
git clone https://github.com/SkyCooper/DjangoTutorial.git

# daha sonra klasör içinde konumlan,
cd DjangoTutorial

# versiyon kontrolü yap,(sonradan lazım olacak unutma)
python --version

# env oluştur,
# versiyon 3 ise;
python -m venv env

# versiyon eski ise,
python3 -m venv env

# ls komutu ile dosyalara bak, (env dosyasını gör)

# env'yi aktif et, LİNUX ortamında olduğumuzdan bu komut.
source env/bin/activate

# terminalin başında (env) var ise, aktif olmuş demektir.

# eğer deploy edilecek proje windows kurulu bir bilgisayarda yapılmış ise;
# pythonanwhere ana sayfasından Files sekmesine git,
# sol taraftaki Directories altından eklediğin klasör ismine bas,
# hemen yanında ki Files bölümünden requirements.txt dosyasına tıklayıp aç,
pywin32==304
# eğer içinde bu varsa sil ve sağ üst köşeden SAVE et,
# windowsa'a özel bir paket olduğundan ve çalıştığımız Bash console LINUX olduğu için
# yükleme esnasında hata veriyor ve altındaki paketleri yüklemiyor.
# eğer mac kullanıcısı isen gerek yok buna,


# artık Bash consoledan requirements paketlerini yükle,
pip install -r requirements.txt

# kurduktan sonra tekrar anasayfadan WEB sekmesine geçiyoruz,
# Add a new web app, --> next
# Manual configuration (including virtualenvs) (BUNU SEÇ)
# versiyonu seç, --> next 

# nameofyourproject.pythonanywhere.com vs gibi bir url oluşturuldu,
# şimdi bazı ayarları düzenlicez.

# Bash console'dan 
pwd
# komutunu yaz --> (/home/coopersky/DjangoTutorial  bu geldi )

# Code: bölümü altındaki alanların ikisinede aynısını yapıştır,
Source code: /home/coopersky/DjangoTutorial
Working directory: /home/coopersky/DjangoTutorial


WSGI configuration file:
# sağ tık, yeni sekmede aç, 74-89 arasındaki DJANGO bölümü hariç alt-üst hepsini sil,
# 1-2 nci satırlardan sonraki bütün satırları yorumdan çıkar,

# pwd ile aldığın yolun aynısını path içine yapıştır,
path = '/home/coopersky/DjangoTutorial'

# mysite yazan yeri main ile değiştir
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'

# Sağ üstten SAVE et.


# Bash console'dan 
cd env
pwd 
# (/home/coopersky/DjangoTutorial/env)
Virtualenv: bölümündeki yere yapıştır.

# pythonanwhere ana sayfasından Files sekmesine git,
# sol taraftaki Directories altından eklediğin klasör ismine bas,
# Files tarafından  .env yaz ve "New File" tıkla, 
(projedeki env dosyasında ne varsa onları ekle,)
SECRET_KEY=&wmy$qpe^z9535mx!d%vuu7a%8_*hx275cttm)s^83!1q_mrj2
ENV_NAME=dev
DEBUG=True
.....
.....
..... (projedeki env dosyasından başka birşey yazılması gerekirse ekle)
# sağ üst köşeden SAVE et,


# Bash console'dan
cd ..
# ana dizine dön, ls yap manage.py görmen gerekli
# eğer doğru yerdeysen,
python manage.py migrate
python manage.py createsuperuser


# pythonanwhere ana sayfasından Web sekmesine git,
# Reload yap ve sonra üstte oluşturduğu url çalıştır.

DisallowedHost 
# bu hatayı verir ise,
# pythonanwhere ana sayfasından Files sekmesine git,
# sol taraftaki Directories altından eklediğin klasör ismine bas,
# sonra yine Directories tarafından main bas ve Files tarafından settings.py dosyasını aç
ALLOWED_HOSTS = ['*'] 
# böyle tırnak içinde yıldız ekle,
# SAVE et

# pythonanwhere ana sayfasından Web sekmesine git,
# Tekrar Reload yap ve sonra üstte oluşturduğu url çalıştır.

api ana sayfası geldi fakat CSS yok ise;
# pythonanwhere ana sayfasından Files sekmesine git,
# sol taraftaki Directories altından eklediğin klasör ismine bas,
# sonra yine Directories tarafından main bas ve Files tarafından settings.py dosyasını aç
STATIC_URL = 'static/' --> herhangi bir yer olabilir, ama best practice bunun altına;
# ekle;
STATIC_ROOT = BASE_DIR / 'static'
# SAVE et

# Bash consoldan;
python manage.py collectstatic
# 165 static files copied to '/home/coopersky/DjangoTutorial/static'.
# yukarıda böyle bir satır dönecek, içinden yolu kopyala,
# pythonanwhere ana sayfasından Web sekmesine git,
Static files:
# bölümünün altındaki URL'ye,
/static/
# Directory yazan yere;
/home/coopersky/DjangoTutorial/static 

# Tekrar Reload yap ve sonra üstte oluşturduğu url çalıştır.
# artık, css yüklenmiş olarak kullanılmaya hazır.




# dev.py içinden debug toolbar ile ilgili ayarları kapat,
from .base import *

DEBUG = config("DEBUG")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        }
}

# bunlar hariç herşey yoruma alınacak,

# buna göre .env dosyası
SECRET_KEY=ginfconh+5hy4ja1ryor%fgdgf
ENV_NAME=dev
DEBUG=True
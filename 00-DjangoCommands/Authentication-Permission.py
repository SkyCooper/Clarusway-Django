Authentication-Permission   
@cooper (01 Şubat 2023, Çarşamba)


#* Authentication için; (dj-09)
# ilave bir paket yüklemeye gerek yok,

# Authentication => bir kişinin ya da bir şeyin iddia ettiği olduğunu doğrulamak için yapılan işlemdir.
# Bu genellikle bir kullanıcı adı ve parola gibi kimlik bilgileri ya da bir parmak izi veya yüz tanıma gibi biyometrik veriler kullanılarak yapılır.

# Authorization =>  doğrulanmış (Authenticate olmuş) kullanıcının izinlerine göre belirli kaynaklara veya eylemlere erişimi verme veya reddetme işlemidir. 
# Örneğin, doğrulanmış bir kullanıcının belirli belgeleri okumaya izin verilmiş olabilir, ancak düzenleme veya silme yetkisi olmayabilir.


#! 1 - settings içine ekleyerek Authentication için izin ver;

#* BASIC authentication :
#? GÜVENSİZdir. Bundan dolayı kullanılmıyor.

# settings içine ekle;
    REST_FRAMEWORK = {
        #* BASIC authentication
        'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.BasicAuthentication'],
    }
# Basic Authentication kullanılan işlemlerde POSTMEN'de;
# Headers altında Authorazation (KEY) karşısında --> Bacic xoxoxoxoxx (VALUE) yazıyor.
# Buradaki xoxoxox giriş yapılan username ve password bilgilerinin Base64 ile şifrelenmiş halidir. 
# Bunu okumak için kopyalayıp https://www.base64decode.org/ gibi sitelere yapıştırırsak username ve password görünür.

    
#* TOKEN Authentication:
#? Güvenliği arttırmak için tercih ediliyor.

# settings içine ekle;
    REST_FRAMEWORK = {
        #* TOKEN authentication                      
        'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication'],
        
        #* TOKEN + BASIC authentication
        'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication',
                                            'rest_framework.authentication.BasicAuthentication']
    }
# Üretilen token kullanıcı aktifken var, logout olunca siliniyor, tekrardan kullanılmıyor.
# INSTALLED_APPS içine ekle. 
INSTALLED_APPS = [ 'rest_framework.authtoken', ]
# Böylece database'de kullanıcıyı ve ona ait Key tutan bir tablo oluşturuyor,
# db değişiklik yaptığı için;
python manage.py migrate
# python manage.py runserver    
    

#* PERMISSION için; (dj-09)

#! 2- Authotantıcatıon yapıldı, sonra permission vermek gerekiyor.

#todo, A- Django default permission kullanma;

# view içine import et,
from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

# kullanılacak viewe ekle ..
permission_classes = [IsAuthenticated] #? (giriş yapan herkes CRUD yapabilir) 
permission_classes = [IsAdminUser] #? (sadece admin olan) CRUD yapabilir
permission_classes = [IsAuthenticatedOrReadOnly] #? Authenticate olan (yani giriş yapan) herşeyi yapar, olmayan sadece GET(read) yapar.


# postmende Authorazation --> No Auth;
# Headers --> Authorazation (Key olarak) bölüm ekle --> karşısına  Token vhfosdbvodjfboıdjboıdjboıj YAZ.
# Token bir Authorazation yöntemi, daha sonra Permission durumuna göre izin verilen işlemleri yapabilir,
# Yani her Token sahibi herşeyi yapamaz, IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly vs. 
# durumuna göre ne kadar izni varsa ona göre işlem yapabilir.

#todo, B- Custom permission yazıp kullanma;
# permissions.py isimli bir dosya oluştur, ve default permissionları override ederek custum permission yaz,

# permissions.py;
from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

class IsStafforReadOnly(permissions.IsAdminUser):
    message = 'You do not have permission perform this action.'
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
        # if request.method = 'GET':  # sadece böylede yazılabilir.
            return True
        return bool(request.user and request.user.is_staff)

# custom permission tanımlarken neye izin vereceğini anlatan bir isim vermek gerekli,
# IsAdminUser'dan customize edeceğimiz için onu import edip inherit ettik
# Bütün permission'lar True/False döner, yani istek yapanın yetkisi varsa True döner ve izin verir.
# Burada GET için True döner, ve her tür kullanıcı GET yapar,
# GET harici bir istek gelirse False olur ve yapmadan aşağıya geçer,
# O zamanda sadece staff ise yani admin ise True döner.

#* SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS') demektir.

class IsOwnerAndStaffOrReadOnly(permissions.BasePermission):
    
    # def has_permission(self, request, view):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return bool(request.user.is_staff and (obj.create_user == request.user))
        



#? herkes okusun ama sadece admin olan create/update yapabilmesi için ilave bir metod yazdık.
#? aslında BasePermission içinde olan IsAuthenticatedOrReadOnly metodunu override ettik

""" override edilen metod;
class IsAuthenticatedOrReadOnly(BasePermission):
    ""
    The request is authenticated as a user, or is a read-only request.
    ""

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )
"""

#? 1nci yöntem; biz yazdık (yapay zeka)
class IsAdminUserOrReadOnly(BasePermission):  #? IsAdminUserOrReadOnly bu ismi  biz yazdık
  """ 
  Buraya metod için açıklayıcı bir docstring yazılabilir.
  Herkes okusun ama sadece admin olan create/update yapabilsin  
  """
  def has_permission(self, request, view):
    if request.method in ['GET']:
      return True
    else:
      return request.user.is_staff



#? 2nci yöntem; sinan hoca yazdı
class IsAdminOrReadOnly(BasePermission):
    # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )

# custom permission yazıldıktan sonra view'da import et
from .permissions import IsAdminOrReadOnly, IsOwnerAndStaffOrReadOnly,IsStafforReadOnly

# daha sonra istediğin view altında kullan,
permission_classes = [IsAdminOrReadOnly]
permission_classes = [IsOwnerAndStaffOrReadOnly]





#! setting.py içindeki örnek bir REST_FRAMEWORK
# hangisi / hanfilerini kullanacaksan kalsın diğerlerini sil/yoruma al.
                
REST_FRAMEWORK = {

    #* BASIC authentication
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.BasicAuthentication'],
    
    #* TOKEN authentication
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication'],
    
    #* TOKEN + BASIC authentication
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication', 'rest_framework.authentication.BasicAuthentication'],
    
}

#! view.py içindeki örnek importlar

#? Permission
from .permissions import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, BasePermission



#* PERMISSION için; (dj-20_StockApp-DjangoDefaultPermission)
# https://www.django-rest-framework.org/api-guide/permissions/#djangomodelpermissions

# admin panelde herhangi bir user'a user bazında bir veya birden fazla permission ataması yapılabiliyor,
# admin panelde Users'tan bir kullanıcı üzerine tıklayınca
# Groups ve User permissions özellikleri ayarlanabiliyor,
# User permissions ile mevcut bütün CRUD işlemlerinden istenilen tek tek seçilebilir,

# Groups ile bir grup oluşturulup, CRUD işlemlerinden istenilen tek tek seçilebilir
# ve user o gruba tanırsa, gruba izin verilen işemleri yapabilir,

# superuser olarak create edilen admin
# veya sonradan superuser olarak işaretlenen user bütün CRUD işlemlerini yapmaya izinlidir.


#? böyle import edilir,
from rest_framework.permissions import DjangoModelPermissions

#? view altına eklenerek kullanılır,
    permission_classes = [DjangoModelPermissions]
# persission kullanılması için Authantice olmak gerekir, onun için postmen kullanırken
# headers için Authorazation ----> Token 16dc6s4c6s4cdv65s4v64sv64s6v46sd yazmak gerekli.

#! view'da sadece yukarıdaki 2 satırı yazarak permission verebiliriz,
#! Gerisini artık her kullanıcı için admin panelden;
#! Groups / User permissions özelliklerini ayarlamak kalıyor.

# ilgili app içine signal.py ekleyerek bir user create edildiğinde
# superuser değilse hangi grupta olsun vs.. gibi bir logic yazabiliriz.

# signals.py
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)  
        user= User.objects.get(username = instance)
        
        #? user'ın grubunu atıyor,
        #? hata vermemesi için önceden Read_Only vaya ismi ne verilecekse o grubun oluşturulmuş olması gerekiyot.
        if not user.is_superuser:
            group = Group.objects.get(name='Read_Only') 
            user.groups.add(group)
            user.save()
            
#! bu örnekte biz superuser olmayan kullanıcılara sadece GET yetkisi verdik,
#! fakat vermesekte superuser olmayan kullanıcıların  DEFAULT get yetkisi vardır.

# app.py (eklemek gerekli)

    #? signal çalışsın diye;
    def ready(self):
        import account.signals


# admin.py (user grup admin panelde görünsün diye)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class UserAdminWithGroup(UserAdmin):
    def group_name(self, obj):
        queryset = obj.groups.values_list('name', flat=True)
        groups = []
        for group in queryset:
            groups.append(group)

        return ' '.join(groups)
    
#?admin panelde user grup görünsün diye;
    list_display = UserAdmin.list_display + ('group_name',)


admin.site.unregister(User)
admin.site.register(User, UserAdminWithGroup)
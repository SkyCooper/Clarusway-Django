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
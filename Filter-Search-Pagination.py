Pagination-Filter-Search-Ordering-Permission   
@cooper (01 Şubat 2023, Çarşamba)

#* PAGINATION İÇİN; (dj-08)
# ilave bir paket yüklemeye gerek yok,
#todo, A- Eğer Djangonun default pagination ayarlarını kullanacaksak, iki farklı şekilde yapılabilir,
        #! 1 - settings içine ekleyerek;
                  # en sonuna hangisini kullanacaksan o kalsın diğer ikili grupları sil
                  # kod yukarıdan aşağıya geldiği için silinmezse en son yazılanı alır.
                  #? böyle yapınca global alanda tanımlanmış olur ve onu kullanır,

                  REST_FRAMEWORK = {
                      'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
                      'PAGE_SIZE': 30,
                      
                      'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.LimitOffsetPagination',
                      'PAGE_SIZE': 30,
                      
                      'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.CursorPagination',
                      'PAGE_SIZE': 30,
                  }
                  
                  # view içinde ilave pagination_class = ............. 
                  # yazmaya gerek olmadan setting içinde hangisi tanımlanmış ise onu alır.

        #! 2 - views içinde import ederek
                  # setting içine birşey yazmaya gerek yok,
                  # fakat yazılsa bile local alanda olan globalı ezeceğinden import edilen çalışacaktır.
                  
                  from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

                  # daha sonra hangisini kullanacaksak view altında yazabiliriz,
                  pagination_class = PageNumberPagination
                  pagination_class = LimitOffsetPagination
                  pagination_class = CursorPagination
                  # (hangisini kullanacaksan adını yaz)

#todo, B- Djangonun default ayarları dışında customize bir pagination kullanmak için, pagination.py ekle;
#? böyle yapınca localde çalışır ve global olanı ezer, yani settings içinde yazılsa bile burada yazılan çalışır,

# pagination.py
from rest_framework.pagination import (
  PageNumberPagination,
  LimitOffsetPagination,
  CursorPagination
  )


class CustomPageNumberPagination(PageNumberPagination):
  page_size = 5
  # 'PAGE_SIZE': 30, ==> settings içinde 30 yazıyor.
  # local'de yazılan globalde yazılanı ezer. onun için onu artık yoruma alabiliriz..
  page_query_param = 'sayfa'          #? artık page yerine sayfa yazıyor.
  
class CustomLimitOffsetPagination(LimitOffsetPagination):
  default_limit = 10
  limit_query_param = 'adet'          #? limit yerine adet
  offset_query_param = 'baslangic'    #? offset yerine başlangıc yazıyor.
  
class CustomCursorPagination(CursorPagination):
  cursor_query_param = 'imlec'        #? cursor yerine imleç
  page_size = 10
  ordering = '-id'                    #? id'ye göre tersten sıralama yapar.


# yapılan paginationı views içine import et,
from .pagination import * # (hepsini ekle demek)

# views.py içindeki view altına;
pagination_class = CustomPageNumberPagination
pagination_class = CustomLimitOffsetPagination
pagination_class = CustomCursorPagination
# (hangisini kullanacaksan adını yaz)



#* FİLTER için; (dj-08)
# yazılan kelimenin aynısını arar,
# mesela name için data içinde cooper varsa coop yazınca bulmaz.

pip install django-filter
pip freeze > requirements.txt


#todo, A- Eğer Djangonun default FILTER ayarlarını kullanacaksak, iki farklı şekilde yapılabilir,
        #! 1 - settings içine ekleyerek;
                  INSTALLED_APPS = [ 'django_filters', ] # içine ekle
                  # en sonuna uygun bir yere DEFAULT_FILTER_BACKENDS ekle,
                  # eğer önceden REST_FRAMEWORK = { } varsa onun içine ekle, yoksa üstteki çalışmaz.
                  #? böyle yapınca global alanda tanımlanmış olur ve onu kullanır,

                  REST_FRAMEWORK = {
                      'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
                  }
                  
                  # view'da filterset_fields ekleyip, filitrelenecek alanları yazıyoruz,
                  filterset_fields = ["id", "first_name", "last_name"]

        #! 2 - views içinde import ederek
                  # settings içine birşey yazmaya gerek yok,
                  # fakat yazılsa bile local alanda olan globalı ezeceğinden import edilen çalışacaktır.
                  
                  from django_filters.rest_framework import DjangoFilterBackend

                  # view'da filter_backends ve filterset_fields ekleyip, filitrelenecek alanları yazıyoruz,
                  filter_backends = [DjangoFilterBackend]                 #? hangi filitrelemeyi kullanacak,
                  filterset_fields = ["id", "first_name", "last_name"]    #? nerede filitrelemeyi kullanacak,
                  # (hangisini kullanacaksan adını yaz)

#todo, B- Djangonun default ayarları dışında customize bir FILTER kullanmak için, filter.py ekle;
#? böyle yapınca localde çalışır ve global olanı ezer, yani settings içinde yazılsa bile burada yazılan çalışır,
# daha sonra paginationda yapıldığı gibi default filter ayarları miras alınarak custom bir filter yazılabilir,
# view'da import edilip kullanılabilir fakat yapılmış bir örnek yok, 






#* SEARCH için; (dj-08)
# ilave bir paket yüklemeden yapıldı fakat öncesinde filter için paket yüklenmişti,
pip install django-filter

# yazılan kelimenin içinde arama yapar,
# mesela name için data içinde cooper varsa coop yazınca bulur.
# aynı zamanda last_name de aramaya dahilse macoopland gibi yazan birşeyide bulur ve 2 sonuç getirir.

#todo, A- Eğer Djangonun default SERACH ayarlarını kullanacaksak, iki farklı şekilde yapılabilir,
        #! 1 - settings içine ekleyerek;
                  INSTALLED_APPS = [ 'django_filters', ] # içine zaten eklenmişti
                  # en sonuna uygun bir yere DEFAULT_FILTER_BACKENDS ekle,
                  # eğer önceden REST_FRAMEWORK = { } varsa onun içine ekle, yoksa üstteki çalışmaz.
                  #? böyle yapınca global alanda tanımlanmış olur ve onu kullanır,

                  REST_FRAMEWORK = {
                      'DEFAULT_FILTER_BACKENDS': ['rest_framework.filters.SearchFilter'],
                      
                      #* önceden filter varsa yanına ekle,
                      'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend', 'rest_framework.filters.SearchFilter'],
                  }
                  
                  # view'da search_fields ekleyip, arama alanları yazıyoruz,
                  search_fields = ["first_name", "last_name"]

        #! 2 - views içinde import ederek
                  # setting içine birşey yazmaya gerek yok,
                  # fakat yazılsa bile local alanda olan globalı ezeceğinden import edilen çalışacaktır.
                  
                  from rest_framework.filters import SearchFilter

                  # view'da filter_backends ve search_fields ekleyip, filitrelenecek alanları yazıyoruz,
                  filter_backends = [SearchFilter]                        #? hangi aramayı kullanacak,
                  filter_backends = [DjangoFilterBackend, SearchFilter]   #* önceden sadece filter için yazılmaşsa yanına eklenebilir,
                  search_fields = ["first_name", "last_name"]             #? nerelerde arama yapacak,
                  # (hangisini kullanacaksan adını yaz, içinde geçeni bulur aynısını aramaz.)
                  search_fields=['^first_name']                           #? baş harfine göre arama yapmak için,
                  
                  #? bir model içindeki foreingnkey olarak tanımlanan field'da arama yapabilmek için
                  search_fields = ["firm__name"]    
                  #? firm ForeinKey olduğundan onun ismine ulaşmak için __(ikialtçizgi) kullanıyoruz.

#todo, B- Djangonun default ayarları dışında customize bir SERACH kullanmak için, serach.py ekle;
#? böyle yapınca localde çalışır ve global olanı ezer, yani settings içinde yazılsa bile burada yazılan çalışır,
# daha sonra paginationda yapıldığı gibi default serach ayarları miras alınarak custom bir search yazılabilir,
# view'da import edilip kullanılabilir fakat yapılmış bir örnek yok, 




#* ORDERING için; (dj-08)
# ilave bir paket yüklemeden yapıldı fakat öncesinde filter için paket yüklenmişti,
pip install django-filter


#todo, Eğer Djangonun default ORDERING ayarlarını kullanacaksak, iki farklı şekilde yapılabilir,
        #! 1 - settings içine ekleyerek;
                  INSTALLED_APPS = [ 'django_filters', ] # içine zaten eklenmişti
                  # en sonuna uygun bir yere DEFAULT_FILTER_BACKENDS ekle,
                  # eğer önceden REST_FRAMEWORK = { } varsa onun içine ekle, yoksa üstteki çalışmaz.
                  #? böyle yapınca global alanda tanımlanmış olur ve onu kullanır,

                  REST_FRAMEWORK = {
                      'DEFAULT_FILTER_BACKENDS': ['rest_framework.filters.OrderingFilter'],
                      
                      #* önceden filter/search varsa yanına ekle,
                      'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend', 'rest_framework.filters.SearchFilter', 'rest_framework.filters.OrderingFilter'],
                  }
                  
                  # view'da ordering_fields ekleyip, sıralama alanları yazıyoruz,
                  ordering_fields = ['first_name','last_name']

        #! 2 - views içinde import ederek
                  # settings içine birşey yazmaya gerek yok,
                  # fakat yazılsa bile local alanda olan globalı ezeceğinden import edilen çalışacaktır.
                  
                  from rest_framework.filters import OrderingFilter

                  # view'da filter_backends ve search_fields ekleyip, filitrelenecek alanları yazıyoruz,
                  filter_backends = [OrderingFilter]                   #? hangi sıralamayı kullanacak,
                  filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]   #* önceden  yazılmaşsa yanına eklenebilir,
                  ordering_fields = ['first_name','last_name']         #? nerelerde sıralama yapacak,
                  ordering = ['last_name']                             #? default olarak ilk açıldığında buraya yazdığımıza göre sıralıyor.
                  
                  



#* PERMISSION için; (dj-09)
# ilave bir paket yüklemeye gerek yok,

# Authentication => bir kişinin ya da bir şeyin iddia ettiği olduğunu doğrulamak için yapılan işlemdir.
# Bu genellikle bir kullanıcı adı ve parola gibi kimlik bilgileri ya da bir parmak izi veya yüz tanıma gibi biyometrik veriler kullanılarak yapılır.

# Authorization =>  doğrulanmış (Authenticate olmuş) kullanıcının izinlerine göre belirli kaynaklara veya eylemlere erişimi verme veya reddetme işlemidir. 
# Örneğin, doğrulanmış bir kullanıcının belirli belgeleri okumaya izin verilmiş olabilir, ancak düzenleme veya silme yetkisi olmayabilir.


#todo, A- Eğer Djangonun default PERMISSION ayarlarını kullanacaksak,
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
    #? pagination
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2,
    
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 5,
    
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.CursorPagination',
    'PAGE_SIZE': 4,
    
    #? filter
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    
    #? search
    'DEFAULT_FILTER_BACKENDS': ['rest_framework.filters.SearchFilter'],

    #? ordering
    # 'DEFAULT_FILTER_BACKENDS': ['rest_framework.filters.OrderingFilter'],
    
    #? filter + search + ordering
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend', 'rest_framework.filters.SearchFilter', 'rest_framework.filters.OrderingFilter'],
    
    #* BASIC authentication
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.BasicAuthentication'],
    
    #* TOKEN authentication
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication'],
    
    #* TOKEN + BASIC authentication
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication', 'rest_framework.authentication.BasicAuthentication'],
    
}

#! view.py içindeki örnek importlar
#? filter
from django_filters.rest_framework import DjangoFilterBackend

#? search
from rest_framework.filters import SearchFilter

#? ordering
from rest_framework.filters import OrderingFilter

#? pagination,
from .pagination import *
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

#? Permission
from .permissions import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, BasePermission
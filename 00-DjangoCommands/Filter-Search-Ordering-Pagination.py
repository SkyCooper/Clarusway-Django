Pagination-Filter-Search-Ordering
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
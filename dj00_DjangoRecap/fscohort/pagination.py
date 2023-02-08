from rest_framework.pagination import (PageNumberPagination, LimitOffsetPagination, CursorPagination)

#? GLOBAL TANIMLAMA : (main --> settings içine yazarak):
# yapılan ayar bütün endpointler için geçerli olur,
# mesela settings içine; 'rest_framework.pagination.PageNumberPagination', 'PAGE_SIZE': 5, yazılırsa
# var olan bütün endpointlerde artık 5'li PageNumberPagination geçerli olur, 

#? LOCAL TANIMLAMA : (view içinde import ederek, default veya customize) :
# Sadece yazılan view'ın endpointinde geçerli olur,
# mesela bir endpoint için 8'li PageNumberPagination yapılırken
# başka birisi için 3'lü CustomLimitOffsetPagination yapılabilir.

#* dikkat edilmesi gereken local olan global olanı zaten ezecektir,
# yani settings içine; 'rest_framework.pagination.PageNumberPagination', 'PAGE_SIZE': 5, yazılırsa
# var olan bütün endpointlerde artık 5'li PageNumberPagination geçerli olur,
# fakat değiştirmek istediğimiz view'da import edip bir CustomPagination kullanırsak
# sadece orası değişir, diğerleri yine aynı kalır.

#? Global / Local kavramı diğer ayarlar (filter , search, ordering vs..) içinde aynı mantıkla çalışır,




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
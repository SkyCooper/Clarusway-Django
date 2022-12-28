from rest_framework.pagination import (
  PageNumberPagination,
  LimitOffsetPagination,
  CursorPagination
  )


class CustomPageNumberPagination(PageNumberPagination):
  page_size = 5
  # 'PAGE_SIZE': 30, ==> settings içinde 30 yazıyor.
# local'de yazılan globalde yazılanı ezer. onun için onu artık yoruma alabiliriz..
  page_query_param = 'sayfa'
  # artık page yerine sayfa yazıyor.
  
class CustomLimitOffsetPagination(LimitOffsetPagination):
  default_limit = 10
  limit_query_param = 'adet'          #? limit yerine adet
  offset_query_param = 'baslangic'    #? offset yerine başlangıc yazıyor.
  
class CustomCursorPagination(CursorPagination):
  cursor_query_param = 'imlec'
  page_size = 10
  ordering = '-id'
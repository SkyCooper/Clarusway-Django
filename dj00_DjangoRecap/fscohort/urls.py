from django.urls import path
from .views import homefs
#? . yani bulunduğu dizin, yani fscohort içinden demek

from .views import student_api, student_api_get_update_delete, path_api

urlpatterns = [
    path('', homefs),
    
    path('student/', student_api),
    path('student/<int:pk>', student_api_get_update_delete, name="detail"),
    # yani ID yazıp ilgili öğrenci bilgisi çekilebilir.
    # HyperlinkedRelatedField ile yapılıp -> view_name='detail' yazıldığığı için name="detail" yazmak gerekli, hata verir.
    
    path('path/', path_api),
]

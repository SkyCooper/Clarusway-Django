from django.urls import path, include

#? VIEWSETS için router import
from rest_framework import routers

from .views import (
    home,
    
    #! function views
    # students_list,
    # student_create,
    # student_detail,
    # student_update,
    # student_delete,
    # student_api,
    # student_api_get_update_delete
    
    #! class views
    #* APIVIEW
    # StudentListCreate,
    # StudentDetail,
    
    #* GENERIC APIVIEW  -  MIXINS
    # StudentGAV,
    # StudentDetailGAV,
    
    #* CONCRETE VIEWS
    # StudentCV,
    # StudentDetailCV,
    
    #* VIEWSETS
    StudentMVS,
    PathMVS
)

#? VIEWSETS için router kurmak ZORUNLU,
router = routers.DefaultRouter() #? router isimli bir instance oluşturduk.
router.register("student", StudentMVS) #? buradaki student prefix
router.register("path", PathMVS)

#* 2 çeşit Router var, Simple ve Default, biz DefaultRouter kullandık,
#* tek farkı [.format] özelliği, bu örnekte /api/.json yazarsak bize bir endpoint veriyor.

urlpatterns = [
    path("", home),
    
    #! function views
    # path("student-list/", students_list, name='list'),
    # path("student-create/", student_create, name='create'),
    # path("student-detail/<int:pk>/", student_detail, name='detail'),
    # path("student-update/<int:pk>/", student_update, name='update'),
    # path("student-delete/<int:pk>/", student_delete, name='delete'),
    # path('student', student_api),
    # path('student/<int:pk>', student_api_get_update_delete)
    
    #! class views
    #? FBV den farkı, sonuna as_views() yazılması
    #* APIVIEW
    # path('student', StudentListCreate.as_view()),
    # path('student/<int:pk>', StudentDetail.as_view()),
    
    #* GENERIC APIVIEW  -  MIXINS
    # path('student', StudentGAV.as_view()),
    # path('student/<int:pk>', StudentDetailGAV.as_view()),
    
    #* CONCRETE VIEWS
    # path('student', StudentCV.as_view()),
    # path('student/<int:pk>', StudentDetailCV.as_view()),
    
    #* VIEWSETS
    #? include ile kullanılıyor ve router'a yönlendirme yapılıyor.
    path('', include(router.urls)),
]

#! böyle de kullanılıyor, karşımıza çıkabilir.
# urlpatterns += router.urls
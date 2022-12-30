from django.urls import path, include
from .views import (home, StudentMVS, PathMVS)

#? VIEWSETS için router import
from rest_framework import routers


#? VIEWSETS için router kurmak ZORUNLU,
router = routers.DefaultRouter() #? router isimli bir instance oluşturduk.
router.register("student", StudentMVS) #? buradaki student prefix
router.register("path", PathMVS)

#* 2 çeşit Router var, Simple ve Default, biz DefaultRouter kullandık,
#* tek farkı [.format] özelliği, bu örnekte /api/.json yazarsak bize bir endpoint veriyor.

urlpatterns = [
    path("", home),
    
    #* VIEWSETS
    #? include ile kullanılıyor ve router'a yönlendirme yapılıyor.
    path('', include(router.urls)),
]

#! böyle de kullanılıyor, karşımıza çıkabilir.
# path('', include(router.urls)), yerine bunu yazsak çalışır.
# urlpatterns += router.urls
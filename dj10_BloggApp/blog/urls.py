from django.urls import path, include

from .views import CategoryView, BlogView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', CategoryView)
router.register('blog', BlogView)


#? 1inci yöntem
urlpatterns = [
    path('', include(router.urls))
]


#? 2nci yöntem
# urlpatterns = router.urls  # yukarıdaki urlpatterns tanımlazmazsa = olmalı


#? 3üncü yöntem
# urlpatterns = [ ]
# urlpatterns += router.urls  # yukarıdaki urlpatterns tanımlnırsa += olmalı
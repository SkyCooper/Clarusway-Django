from django.urls import path, include

from .views import CategoryView, BlogView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', CategoryView)
router.register('blog', BlogView)


urlpatterns = [
    path('', include(router.urls))
]

# urlpatterns += router.urls

from django.urls import path
from .views import homeds
#? . yani bulunduğu dizin, yani dscohort içinden demek


urlpatterns = [
    path('', homeds),
]

from django.urls import path
from .views import homefs
#? . yani bulunduğu dizin, yani fscohort içinden demek

urlpatterns = [
    path('', homefs),
]

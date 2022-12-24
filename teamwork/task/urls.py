from django.urls import path
from .views import artist_list


urlpatterns = [
    path('', artist_list),
]
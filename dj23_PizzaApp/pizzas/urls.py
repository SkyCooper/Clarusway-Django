from django.urls import path
from .views import home, pizzas

urlpatterns = [
    path('', home, name='home'),
    path('pizzas/', pizzas, name='pizzas'),
]
from django.urls import path
from .views import homeaws

urlpatterns = [
  path('', homeaws),
]
from django.urls import path
from .views import RegisterView

from rest_framework.authtoken import views

urlpatterns = [
    path("register/", RegisterView.as_view()),
    #? obtain_auth_token bir login endpoint  oluşturuyor. username ve password giriliyor,
    #? db'de eğer bu user için bir token varsa onu getiriyor, yoksa yeni bir token create ediyor ve onu getiriyor.
    path('login/', views.obtain_auth_token),
]
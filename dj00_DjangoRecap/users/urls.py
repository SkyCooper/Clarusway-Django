from django.urls import path,include
from .views import RegisterView

#? login/logout için;
from .views import logout
from rest_framework.authtoken import views

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    #? dj_rest_auth, paketi içinde default url'ler mevcut;
    #? bunu kullanınca ilave login/logout url tanımlamaya gerek yok.
        # user/ auth/ password/reset/ [name='rest_password_reset']
        # user/ auth/ password/reset/confirm/ [name='rest_password_reset_confirm']
        # user/ auth/ login/ [name='rest_login']
        # user/ auth/ logout/ [name='rest_logout']
        # user/ auth/ user/ [name='rest_user_details']
        # user/ auth/ password/change/ [name='rest_password_change']
    
    path("register/", RegisterView.as_view()),
        # user/ register/
    
    # path('login/', views.obtain_auth_token),
    #? obtain_auth_token bir login endpoint  oluşturuyor. username ve password giriliyor,
    #? db'de eğer bu user için bir token varsa onu getiriyor, yoksa yeni bir token create ediyor ve onu getiriyor.
        # user/ login/
    
    # path('logout/', logout),
        # user/ logout/
]
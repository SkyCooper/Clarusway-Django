from django.contrib import admin
from django.urls import path, include
from .views import real_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', real_home),
    path("api/", include("student_api.urls")),
    path("user/", include("user.urls")),
]

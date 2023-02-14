from django.urls import path, include
from .views import home, student_list

urlpatterns = [
    path('', home, name="home"),
    path('list', student_list, name="student_list"),
]

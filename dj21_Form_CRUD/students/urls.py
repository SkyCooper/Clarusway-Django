from django.urls import path, include
from .views import (
    home,
    student_list,
    student_add,
    student_update
    )

urlpatterns = [
    path('', home, name="home"),
    path('list/', student_list, name="student_list"),
    path('add/', student_add, name="student_add"),
    path('update/<int:id>', student_update, name="student_update"),
]

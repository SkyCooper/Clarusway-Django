from django.urls import path, include
from .views import (
    home,
    student_list,
    student_add,
    student_update,
    student_detail,
    student_delete,
    )

urlpatterns = [
    path('', home, name="home"),
    path('list/', student_list, name="student_list"),
    path('add/', student_add, name="student_add"),
    path('update/<int:id>', student_update, name="student_update"),
    path('detail/<int:id>', student_detail, name="student_detail"),
    path('delete/<int:id>/', student_delete, name="student_delete"),
]

#! burada name kullanmanın amacı, 
# name için istediğimiz ismi yazabiliriz, 
# kullanma mantığı şöyle, bir sayfada name kullanırsak, path değişse bile hata vermez,
# fakat path kullanırsak, path değişince hangi sayfada kullandıysak oranında değişmesi lazım.
# Mesela view'da kullanımı
    # 1-name; redirect("student_list")
    # 2-path; redirect("/list")
    # eğer urls.py içinden path api/student/list vs. gibi değişse 1 numara yinede çalışır,
    # fakat 2 numara hata verir, redirect("/api/student/list") tekrar böyle düzenlemek gerekir.
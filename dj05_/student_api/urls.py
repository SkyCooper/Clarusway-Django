from django.urls import path
from .views import home , student_api, student_api_get_update_delete, path_api

urlpatterns = [
    path("", home),
    path("student/", student_api),
    path("student/<int:pk>", student_api_get_update_delete, name="detail"),
    path("path/", path_api)
]

from django.urls import path,include
from .views import *
# from rest_framework import routers

# router = routers.BaseRouter()


urlpatterns = [
    path("department/", DepartmentView.as_view()),
    path("personal/", PersonalListCreateView.as_view()),
    path("personal/<int:pk>/",PersonalGetUpdateDelete.as_view()),
    path("department/<str:department>/",DynamicDepartmentView.as_view()),
    # path("department/<str:name>/",CustomDynamicDepartmentView.as_view()),
]
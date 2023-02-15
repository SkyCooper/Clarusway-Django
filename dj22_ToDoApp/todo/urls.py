from django.urls import path
from .views import (
    todo_list,
)

urlpatterns = [
    path('list/', todo_list, name='todo_list'),
]
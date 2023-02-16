from django.urls import path
from .views import (
    todo_list,
    todo_add1,
    todo_add2,
    todo_update,
    todo_delete,
    
    todo_detail,
)

urlpatterns = [
    path('list/', todo_list, name='todo_list'),
    
    # sinan ve henry hocanın yazdığı 2 farklı yöntemle denedim, ikiside çalıştı..
    path('add1/', todo_add1, name='todo_add1'),
    path('add2/', todo_add2, name='todo_add2'),
    
    path('update/<int:pk>', todo_update, name='todo_update'),
    path('delete/<int:pk>', todo_delete, name='todo_delete'),
    
    path('detail/<int:pk>', todo_detail, name='todo_detail'),
]
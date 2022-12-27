from django.urls import path, include

#? VIEWSETS için router import
from rest_framework import routers

#* FUNCTION VIEW
from .views import (
    # todo_list_create,
    # todo_detail
    todo_home
    )

#* CONCRETE VIEWS
# from .views import Todos, TodoDetail

#* VIEWSETS
from .views import TodoMVS


#? VIEWSETS için router kurmak ZORUNLU,
router = routers.DefaultRouter()
router.register('todo', TodoMVS)

urlpatterns = [
    path('', todo_home),
    
    #* FUNCTION VIEW
    # path('list-create/', todo_list_create),
    # path('detail/<int:pk>', todo_detail)
    
    #* CONCRETE VIEWS
    # path('list-create/', Todos.as_view()),
    # path('detail/<int:pk>', TodoDetail.as_view())
    
    #* VIEWSETS
    #? include ile kullanılıyor ve router'a yönlendirme yapılıyor.
    path('', include(router.urls))
]

#* path('', include(router.urls)) bunu yazmadan aşağıdakini yazsak da çalışır.
#! urlpatterns += router.urls
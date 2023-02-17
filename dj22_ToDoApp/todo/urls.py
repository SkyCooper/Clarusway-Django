from django.urls import path

#? FBV imports
from .views import ( todo_list, todo_add1, todo_add2,todo_update,todo_delete, todo_detail,)


#? hem FBV hemde CBV çalışsın diye pathler listfb ve listcb gibi düzenlendi

#? FBV urls,
urlpatterns = [
    path('listfb/', todo_list, name='todo_listfb'),
    
    # sinan ve henry hocanın yazdığı 2 farklı yöntemle denedim, ikiside çalıştı..
    path('addfb1/', todo_add1, name='todo_add1fb'),
    path('addfb2/', todo_add2, name='todo_add2fb'),
    
    path('updatefb/<int:pk>', todo_update, name='todo_updatefb'),
    path('deletefb/<int:pk>', todo_delete, name='todo_deletefb'),
    
    path('detailfb/<int:pk>', todo_detail, name='todo_detailfb'),
]


#?CBV imports
from .views import ( TodoListView,TodoCreateView, TodoUpdateView, TodoDeleteView, TodoDetailView )


#? CB olduğundan .as_view() kullanmak gerekiyor.
#? CBV urls,
urlpatterns += [
    path('listcb/',TodoListView.as_view(),name='todo_listcb' ),
    path('addcb/',TodoCreateView.as_view(),name='todo_addcb' ),
    path('updatecb/<int:pk>',TodoUpdateView.as_view(),name='todo_updatecb' ),
    path('deletecb/<int:pk>',TodoDeleteView.as_view(),name='todo_deletecb' ),
    path('detailcb/<int:pk>', TodoDetailView.as_view(), name="todo_detailcb"),
]
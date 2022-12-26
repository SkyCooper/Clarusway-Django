from django.urls import path
from .views import (
    home,
    
    #! function views
    # students_list,
    # student_create,
    # student_detail,
    # student_update,
    # student_delete,
    # student_api,
    # student_api_get_update_delete
    
    #! class views
    #* APIVIEW
    # StudentListCreate,
    # StudentDetail,
    
    #* GENERIC APIVIEW  -  MIXINS
    # StudentGAV,
    # StudentDetailGAV,
    
    #* CONCRETE VIEWS
    StudentCV,
    StudentDetailCV
    
    
)

urlpatterns = [
    path("", home),
    
    #! function views
    # path("student-list/", students_list, name='list'),
    # path("student-create/", student_create, name='create'),
    # path("student-detail/<int:pk>/", student_detail, name='detail'),
    # path("student-update/<int:pk>/", student_update, name='update'),
    # path("student-delete/<int:pk>/", student_delete, name='delete'),
    # path('student', student_api),
    # path('student/<int:pk>', student_api_get_update_delete)
    
    #! class views
    #? FBV den farkı, sonuna as_views() yazılması
    #* APIVIEW
    # path('student', StudentListCreate.as_view()),
    # path('student/<int:pk>', StudentDetail.as_view()),
    
    #* GENERIC APIVIEW  -  MIXINS
    # path('student', StudentGAV.as_view()),
    # path('student/<int:pk>', StudentDetailGAV.as_view()),
    
    #* CONCRETE VIEWS
    path('student', StudentCV.as_view()),
    path('student/<int:pk>', StudentDetailCV.as_view()),
]

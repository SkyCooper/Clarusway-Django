from django.urls import path
from .views import (get_artist_list, 
                    post_artist_list, 
                    artist_list, 
                    artist_detail, 
                    artist_update)


urlpatterns = [
    path('artist/get/', get_artist_list),
    path('artist/post/', post_artist_list),
    path('artist/', artist_list),
    path('artist/<int:pk>', artist_detail),
    path('artist/put/<int:pk>', artist_update),
]
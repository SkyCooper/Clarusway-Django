from django.urls import path
    
#? artist views;
from .views import (
    get_artist_list,
    post_artist_list,
    artist_list,
    artist_detail,
    artist_update,
    artist_delete,
    artist_update_delete,
    song_lyric)

#? album views;
from .views import (
    get_album_list,
    post_album_list,
    get_album_detail,
    album_update,
    album_delete,
    album_list,
    album_get_update_delete
)

#? lyric views;


#? song views;


urlpatterns = [
    #! artist paths;
    path('artist/get/', get_artist_list),
    path('artist/post/', post_artist_list),
    path('artist/', artist_list),
    path('artist/<int:pk>', artist_detail),
    path('artist/put/<int:pk>', artist_update),
    path('artist/delete/<int:pk>', artist_delete),
    path('artist/updatedelete/<int:pk>', artist_update_delete),
    
    #! album paths;
    path('album-list/get', get_album_list),
    path('album-list/<int:pk>', get_album_detail),
    path('album-update/', post_album_list),
    path('album-update/<int:pk>', album_update),
    path('album-delete/<int:pk>', album_delete),
    path('album-list/', album_list),
    path('album-all/<int:pk>', album_get_update_delete),
    
    #! lyric paths;
    
    #! song paths;
    path('artist/song/', song_lyric),
]
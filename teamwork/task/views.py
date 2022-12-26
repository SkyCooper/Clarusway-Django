from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import (
  Artist,
  Album,
  Song,
  Lyric
)

from .serializer import (
  AlbumSerializer,
  ArtistSerializer,
  SongSerializer,
  LyricSerializer,
  SongLyricSerializer
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# def artist_list(request):
#   return HttpResponse("Welcome TASK page")

#? Artist views;

@api_view(['GET'])
def get_artist_list(request):
  artists = Artist.objects.all()
  serializer = ArtistSerializer(artists, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def post_artist_list(request):
  serializer = ArtistSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    message = {
      "message" : "Updated POST"
    }
    # return Response(serializer.data)
    return Response(message, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view() #default get
def artist_detail(request, pk):
  # artist = Artist.objects.get(id=pk)
  artist = get_object_or_404(Artist, id=pk)
  serializer = ArtistSerializer(artist)
  return Response(serializer.data)
    
@api_view(['PUT'])
def artist_update(request, pk):
  artist = get_object_or_404(Artist, id=pk)
  serializer = ArtistSerializer(instance=artist, data=request.data)
  if serializer.is_valid():
    serializer.save()
    message = {
      "message" : "Updated PUT"
    }
    return Response(message, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def artist_delete(request, pk):
  artist = get_object_or_404(Artist, id=pk)
  artist.delete()
  message = {
      "message" : "Artist DELETED"
    }
  return Response(message)

@api_view(['GET', 'POST'])
def artist_list(request):
  if request.method == 'GET':
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = ArtistSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      message = {
      "message" : "Updated POST"
    }
      return Response(message, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT', 'DELETE'])
def artist_update_delete(request, pk):
  if request.method == 'PUT':
    artist = get_object_or_404(Artist, id=pk)
    print(artist)
    serializer = ArtistSerializer(instance=artist, data=request.data)
    if serializer.is_valid():
      serializer.save()
      message = {
      "message" : "Artist Updated"
    }
      return Response(message, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    artist = get_object_or_404(Artist, id=pk)
    artist.delete()
    message = {
        "message" : "Artist DELETED"
      }
    return Response(message)
  
  
#? Album views;

@api_view(['GET'])
def get_album_list(request):
  albums = Album.objects.all()
  serializer = AlbumSerializer(albums, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def post_album_list(request):
  serializer = AlbumSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    message = {"message" : "Album UPDATED"}
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_album_detail(request, pk):
  album = get_object_or_404(Album, id=pk)
  serializer = AlbumSerializer(album)
  return Response(serializer.data)

@api_view(['PUT'])
def album_update(request, pk):
  album = get_object_or_404(Album, id=pk)
  serializer = AlbumSerializer(instance=album, data=request.data)
  if serializer.is_valid():
    serializer.save()
    message = {"message" : "Album UPDATED sucesfully.."}
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def album_delete(request, pk):
  album = get_object_or_404(Album, id=pk)
  album.delete()
  message = {"message" : "Album DELETED"}
  return Response(message)

@api_view(['GET', 'POST'])
def album_list(request):
  if request.method == 'GET':
    albums = Album.objects.all()
    serializer = AlbumSerializer(albums, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = AlbumSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      message = {"message" : "Album UPDATED"}
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def album_get_update_delete(request, pk):
  album = get_object_or_404(Album, id=pk)
  
  if request.method == 'GET':
    serializer = AlbumSerializer(album)
    return Response(serializer.data)
  
  elif request.method == 'PUT':
    serializer = AlbumSerializer(instance=album, data=request.data)
    if serializer.is_valid():
      serializer.save()
      message = {"message" : "Album UPDATED sucesfully.."}
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
  
  elif request.method == 'DELETE':
    album.delete()
    message = {"message" : "Album DELETED"}
    return Response(message)
    
  elif request.method == 'PATCH':
    serializer = AlbumSerializer(album, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      message = {"message" : "Album updated PATCH"}
      return Response(message)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      


#? Lyric views;




#? Song views;

  
@api_view()
def song_lyric(request):
  detailsong = Song.objects.all()
  serializer = SongLyricSerializer(detailsong, many=True)
  return Response(serializer.data)
  

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
  LyricSerializer
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# def artist_list(request):
#   return HttpResponse("Welcome TASK page")

@api_view(['GET'])
def get_artist_list(request):
  artists = Artist.objects.all()
  serializer = ArtistSerializer(artists, many=True)
  return Response(serializer.data)

@api_view() #default get
def artist_detail(request, pk):
  # artist = Artist.objects.get(id=pk)
  artist = get_object_or_404(Artist, id=pk)
  serializer = ArtistSerializer(artist)
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

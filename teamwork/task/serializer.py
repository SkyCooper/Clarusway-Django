from rest_framework import serializers
from .models import (
  Artist,
  Album,
  Lyric,
  Song
)

class ArtistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Artist
    fields = ["first_name", "last_name"]
    
class AlbumSerializer(serializers.ModelSerializer):
  class Meta:
    model = Album
    fields = ["artist", "name"]
    
class LyricSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lyric
    fields = ["title", "content"]
    
class SongSerializer(serializers.ModelSerializer):
  class Meta:
    model = Song
    fields = ["name", "artist"]
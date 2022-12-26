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
    fields = "__all__"
    # fields = ["first_name", "last_name"]
    
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

class SongLyricSerializer(serializers.ModelSerializer):
    items = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Lyric
        fields = ["title","items"]
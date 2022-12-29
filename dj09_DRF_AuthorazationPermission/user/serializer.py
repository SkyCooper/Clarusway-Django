from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#1 nci yöntem
from django.contrib.auth.models import User
#2 nci yöntem
# from django.conf import settings
# settings.AUTH_USER_MODEL

class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
  # email default required değil, onu değiştirdik,
  password = serializers.CharField(write_only=True) #write_only sadece POST, PUT için kullan
  # password zaten required olduğundan yazmadık,
  password2 = serializers.CharField(write_only=True, required=True) #confirmation için
  first_name = serializers.CharField(required=True)
  
  class Meta:
    model= User
    fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'password2')
    
  def validate(self, data):
      if data['password'] != data['password2']:
          raise serializers.ValidationError(
              {'password': 'Password fields didnt match.'}
          )
      return data

  def create(self, validated_data):
    validated_data.pop('password2') # create için gerekli olmadığından dictten çıkardık
    password = validated_data.pop('password') # password sonradan set etmek için değikene atadık.
    user = User.objects.create(**validated_data) # unpack yapıldı, username=validate_data['username], email = va.......
    user.set_password(password) # password ün encrypte olarak db ye kaydedilmesiniş sağlıyor.
    user.save()
    return user
from rest_framework import serializers
from django.contrib.auth.models import User  # (default user modeli import ediyoruz)
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer

#? ilave porfile modeli
from .models import Profile

class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators = [UniqueValidator(queryset=User.objects.all())]
        )
    # email default required değil, onu değiştirdik, artık zorunlu alan
    # email uniq olsun, değilse validation error dönsün onun için ekledik ve yukarıda import ettik (UniqueValidator)
    
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password],
        style = {"input_type" : "password"}
    )
    password2 = serializers.CharField(
        write_only = True,
        required = True,
        style = {"input_type" : "password"}
    )
    # confirmation için tanımlandı, aslında modelde yok onun için zorunlu tanımladık.
    
    # first_name = serializers.CharField(required=True)
    # first_name zorunlu olsun isteseydik böyle yapmak gerekirdi.
  
#! yukarıdakileri yazmadan sadece aşağıdakini yazarsak User modeli birebir kopyalamış oluruz, biz yukarıdakileri yazarak İnherit aldığımız modeli override ettik, kendimize göre customize yaptık.  

    class Meta:
        model = User
        fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'password',
        'password2']
    # bunlar User model'de olan alanlar, + password2 biz ekledik.

  #? Yeni oluşturduğumuz password2 ile password aynımı, bunu konrtol etmek için validate metodunu ekliyoruz.
  #? yazılan metodlarda indentation önemli, class Meta ile aynı hizada,
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {'password': 'Password fields didnt match.'}
            )
        return data

  #? ModelSerializer kullanınca create metodu yazmaya gerek yok aslında fakat, User model içinde olmayan bir field 
  #? (password2) kullandığımız için creat metodunu override etmek gerekli;
  
    def create(self, validated_data): # best practise validated_data yazılır.
        validated_data.pop('password2') # password2 create için gerekli olmadığından dictten çıkardık
        password = validated_data.pop('password') # password sonradan set etmek için dictten çıkardık ve değikene atadık.
        user = User.objects.create(**validated_data) # unpack yapıldı, username=validate_data['username], email = va.......
        # validated_data içinde artık password ve password2 yok, onu kullanarak yeni bir user create edildi.
        user.set_password(password) 
        # yukarıda değişkene atanan password, create edilen user'a atandı,  encrypte olarak db ye kaydedildi.
        user.save()
        # passwor eklenmiş yeni user save edildi.
        return user

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email")
        
class CustomTokenSerializer(TokenSerializer):
    user = UserTokenSerializer(read_only = True)
    
    class Meta(TokenSerializer.Meta):
        fields = ("key", "user")
        
#? ilave porfile serializer
class ProfileSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField(required=False)
    
    class Meta:
        model = Profile
        fields = ("id","user","user_id", "display_name","avatar", "bio")
        
#! buradaki ProfileSerializer'ın kullanıldığı view (ProfileUpdateView)
#! RetrieveUpdateAPIView'dan inherit edildiği için create metodu değil update metodu override edilmeli,        
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.user_id = self.context['request'].user.id
        instance.save()
        return instance
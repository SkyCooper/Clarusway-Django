from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Profile

from dj_rest_auth.serializers import TokenSerializer

class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators = [UniqueValidator(queryset=User.objects.all())]
        )
    
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
    
    class Meta:
        model = User
        fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'password',
        'password2']
        
    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                {"message" : "Password fields didnt match!"}
            )
        return data
    
    
    def create(self, validated_data):
        password = validated_data.get("password")
        validated_data.pop("password2")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    
class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email")
    
    
class CustomTokenSerializer(TokenSerializer):
    user = UserTokenSerializer(read_only = True)
    
    class Meta(TokenSerializer.Meta):
        fields = ("key", "user")


#? profile'ları görmek / update etmek için bir serializer tanımlıyoruz.
#! bir user oluşturulduğunda, otomatik olarak profil oluşması için signals.py de metod yazdık,
#! bir şeyin oluşması başka birşeye bağlı ise signal kullanıyoruz.
class ProfileSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField(required=False)
    
    class Meta:
        model = Profile
        fields = ("id","user","user_id", "display_name","avatar", "bio")
        
#! buradaki ProfileSerializer'ın kullanıldığı view (ProfileUpdateView)
#! RetrieveUpdateAPIView'dan inherit edildiği için create metodu değil update metodu override edilmeli, 
#? user_id istek yapan user'dan alması için;        
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        # validated_data'dan gelen bilgiler ile parentteki update metodunu aynen yap
        # instance güncelle, (buradaki instance her bir profil)
        
        instance.user_id = self.context['request'].user.id
        # sonra bu instance içine user_id ekle, ve ona istek yapan user id'sini ata
        
        instance.save()
        # save et
        return instance
        # return et
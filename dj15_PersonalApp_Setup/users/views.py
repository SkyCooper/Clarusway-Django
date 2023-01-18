from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, ProfileSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Profile
from .permissions import IsOwnerOrStaff
from rest_framework.permissions import IsAuthenticated

class RegisterAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.get(user=user)
        data = serializer.data
        data["key"] = token.key
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
    

#? Profile sayfasını görmek / update etmek için RetrieveUpdateAPIView kullanıyoruz,
class ProfileUpdateView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    
    #* herkes bütün profillere erişmesin diye permission tanımlıyoruz,
    #* giriş yapmış/authentice olmuş, ve admin veya istek yapan kendisi ise
    permission_classes = [IsOwnerOrStaff, IsAuthenticated]
    
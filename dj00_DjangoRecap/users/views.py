from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token

from .serializers import RegisterSerializer
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.generics import RetrieveUpdateAPIView
from .permissions import IsOwnerOrStaff
from rest_framework.permissions import IsAuthenticated


#! register için;
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
#! yeni bir user oluşturulduğunda onun için token oluşturması için yazılan metod;
#! bu bize register olduktan sonra tekrar login sayfasına gitmeden login olmamızı sağlıyor.
#! bunu da user create ediliğinde dönen Response içine key field'nı ekleyerek yapıyor.

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.get(user=user)
        data = serializer.data
        data["key"] = token.key
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


#? dj_rest_auth, paketi içinde default url'ler mevcut;
#? bunu kullanınca ilave login/logout view tanımlamaya gerek yok.   

#! login için;
# ilave metod yazılmadan django'nun view içindeki obtain_auth_token kullandık.

#! logout için;
@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({"message": 'User Logout: Token Deleted'})




#! profile için;
class ProfileUpdateView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsOwnerOrStaff, IsAuthenticated]
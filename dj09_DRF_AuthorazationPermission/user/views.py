from .serializer import RegisterSerializer
from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
#! register için;
class RegisterView(CreateAPIView):
  queryset = User.objects.all()
  serializer_class = RegisterSerializer
  
  #! yeni bir user oluşturulduğunda onun için token oluşturması için yazılan metod;
  #! bu bize register olduktan sonra tekrar login sayfasına gitmeden login olmamızı sağlıyor.
  #! bunu da user create ediliğinde dönen Response içine token field'nı ekleyerek yapıyor.
   
  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    token = Token.objects.create(user_id=response.data['id'])
    response.data['token'] = token.key
    #? burada Response içine token field eklendi.
    # print(response.data)
    return response
  


#! login için;
# ilave metod yazılmadan django'nun view içindeki obtain_auth_token kullandık.

#! logout için;

@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({"message": 'User Logout: Token Deleted'})
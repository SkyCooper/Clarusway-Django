from .serializer import RegisterSerializer
from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token

# Create your views here.
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
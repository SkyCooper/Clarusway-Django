from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

#* signal kullanarak token oluşturma,
#* signal'in görevi = başka bir olayı trgger etme / tetikleme,

#? register olunca token oluşması signal ile yapıldığında models.py içinde yazılması lazım ama 
#? kalabalık olmasın diye signals.py dosyası oluşturulup orada yapmak daha uygun


#! yeni bir user oluşturulduğunda ona token oluşturması için receiver dekoratoru ile yazılan metod;
#! bu bize register olduktan sonra tekrar login sayfasına gitmeden login olmamızı sağlıyor.

#? post_save , yani işlem/olay  bittikten sonra, yani user create edildikten sonra
#? sender=User, User tablosundan yeni user create edilince singnal gönder ve bunu reciver dekaratoru ile yakala

@receiver(post_save, sender=User)
def create_Token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
#? model içine yazmayıp signals.py olarak ayrı bir dosyada yazdığımız için apps.py içine eklemek gerekli
#? apps.py otomatik çalışan bir dosyadır.   ->  signals.py dosyasını çağırır.
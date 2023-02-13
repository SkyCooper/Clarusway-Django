from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group


#? burası token üretiyor,
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)  
        user= User.objects.get(username = instance)
        
        #? user'ın grubunu atıyor,
        #? hata vermemesi için önceden Read_Only vaya ismi ne verilecekse o grubun oluşturulmuş olması gerekiyor.
        if not user.is_superuser:
            group = Group.objects.get(name='Read_Only') 
            user.groups.add(group)
            user.save()
            
#! bu örnekte biz superuser olmayan kullanıcılara sadece GET yetkisi verdik,
#! fakat vermesekte superuser olmayan kullanıcıların  DEFAULT get yetkisi vardır.
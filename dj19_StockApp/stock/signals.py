from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Purchases, Sales, Product

#! yeni bir user oluşturulduğunda ona token oluşturması için receiver dekoratoru ile yazılan metod;
#! bu bize register olduktan sonra tekrar login sayfasına gitmeden login olmamızı sağlıyor.

#? post_save , yani işlem/olay  bittikten sonra, yani user create edildikten sonra
#? sender=User, User tablosundan yeni user create edilince singnal gönder ve bunu reciver dekaratoru ile yakala

@receiver(post_save, sender=Purchases)
def increase_stock(sender, instance, created, **kwargs):
    if created:
        product = Product.objects.get(id=instance.product_id)
        product.stock += instance.quantity
        product.save()
        
@receiver(post_save, sender=Sales)
def decrease_stock(sender, instance, created, **kwargs):
    if created:
        product = Product.objects.get(id=instance.product_id)
        product.stock -= instance.quantity
        product.save()
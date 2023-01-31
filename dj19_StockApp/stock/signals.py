from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Purchases, Sales, Product


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



#! Abdullah hocanın çift kayıt yapan signal kodu,       
 
# @receiver(post_save, sender=Purchases)
# def update_stock_purchases(sender, instance, **kwargs):
#     print('signal çalıştı', instance.product.stock)
#     instance.product.stock += instance.quantity
#     instance.product.save()
#     print('signal çalıştı2', instance.product.stock)
    
    
# @receiver(post_save, sender=Sales)
# def update_stock_sales(sender, instance, **kwargs):
#     instance.product.stock -= instance.quantity
#     instance.product.save()
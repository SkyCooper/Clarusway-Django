from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Purchases, Sales


#? pre_save --> yani DB'ye kayıt edilmeden önce price_total hesaplansın diye;
#? çünkü price_total null=True değil, öyle olsaydı önce null değer atar
#? daha sonra post_save ile de yapabilirdik, (o zaman created da eklemek gerekirdi)
#? fakat pre_save kayıttan önce işlem yaptığı için created gerek yok, (sender, instance, **kwargs) bunlar yeterli,

@receiver(pre_save, sender=Purchases)
def calculate_total_price(sender, instance, **kwargs):
    instance.price_total = instance.quantity * instance.price
    
    
#! signal kullanınca apps.py içine ready metodunu eklemeyi UNUTMA!!!!
    # def ready(self):
    #     import stock.signals
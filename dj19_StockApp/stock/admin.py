from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Firm)
admin.site.register(Purchases)
admin.site.register(Sales)
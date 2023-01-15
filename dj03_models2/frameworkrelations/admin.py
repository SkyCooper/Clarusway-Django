from django.contrib import admin
from .models import Creator, Languages, Frameworks, Programmer
# Register your models here.
admin.site.register(Creator)
admin.site.register(Languages)
admin.site.register(Frameworks)
admin.site.register(Programmer)
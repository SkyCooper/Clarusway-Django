from django.contrib import admin
from .models import Student,Path
from .models import Profile, Address, Product
# Register your models here.

admin.site.register(Student)
admin.site.register(Path)


admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(Product)
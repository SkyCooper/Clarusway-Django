from django.contrib import admin
from .models import Profile

admin.site.register(Profile)

#? Custom User model için 1 numaralı yöntemi kullansaydık;
#? admin panalde bizim oluşturduğumuz MyUser modelinin django tarafından takip edilmesi için ;
# Register your models here.
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.admin import UserAdmin
# from .models import MyUser
# from  django.contrib.auth.forms import UserChangeForm

# class UserAdmin(BaseUserAdmin):
#    form = UserChangeForm
#    fieldsets = (
#        (None, {'fields': ('email', 'password', )}),
#        (('Personal info'), {'fields': ('first_name', 'last_name')}),
#        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
#                                       'groups', 'user_permissions')}),
#        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
#          (('user_info'), {'fields': ('native_name', 'phone_no')}),
#    )
#    add_fieldsets = (
#        (None, {
#            'classes': ('wide', ),
#            'fields': ('email', 'password1', 'password2'),
#        }),
#    )
#    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'native_name', 'phone_no']
#    search_fields = ('email', 'first_name', 'last_name')
#    ordering = ('email', )
# admin.site.register(MyUser, UserAdmin)

#! eğer yukarıdaki ayarları yapmaz isek admin panel'de django default User modelini yakip etmeye devam eder.
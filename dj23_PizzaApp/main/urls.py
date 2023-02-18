from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pizzas.urls')),
    
    #? register/login/logout işlemleri için ilave bir app yazdık, ve oraya yönlendirdik
    path('users/', include('users.urls')),
]

#? images/pillow çaılşması için;
from django.conf import settings
from django.conf.urls.static import static

urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
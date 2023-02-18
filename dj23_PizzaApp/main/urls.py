from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pizzas.urls')),
    path('users/', include('users.urls')),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
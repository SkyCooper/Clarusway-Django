from django.contrib import admin
from django.urls import path,include
# Three modules for swagger:
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# images için;
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
    title="Flight Reservation API", 
    default_version="v1",
    description="Flight Reservation API project provides flight and reservation info",
    terms_of_service="#", 
    contact=openapi.Contact(email="rafe@clarusway.com"), # Change e-mail on this line!
    license=openapi.License(name="BSD License"),),
    public=True, 
    permission_classes=[permissions.AllowAny],
    )


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    # Url paths for swagger:
    path("swagger(<format>\.json|\.yaml)",schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0),name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path('__debug__/', include('debug_toolbar.urls')),
]

#? eklenen imageler browserdan açmak için ilave url tanımlanıyor.
if settings.DEBUG:
    # yani True ise ; development ortamında demektir. o zaman url çalışır
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

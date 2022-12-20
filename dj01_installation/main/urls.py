"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

#! 2-kendi url dosyasından yönlendirme
from django.urls import path, include


#! 1-ayrı ayrı yönlendirme yapma
# from django.urls import path
# from fscohort.views import homefs
# from dscohort.views import homeds
# from awscohort.views import homeaws

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #! 1-ayrı ayrı yönlendirme yapma
    # path('fs', homefs),
    # path('ds', homeds),
    # path('aws', homeaws),
    
    #! 2-kendi url dosyasından yönlendirme
    #* her dosyanın içine urls.py isimli bir dosya oluşturulur.
    path('fs/', include('fscohort.urls')),
    path('ds/', include('dscohort.urls')),
    path('aws/', include('awscohort.urls')),
    
    
]

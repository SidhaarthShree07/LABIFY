"""
URL configuration for Labify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path , include
from myapp.views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home,name='Home'),
    path('home2/', home2,name='home2'),
    path('Lab/',Lab,name='Lab'),
    path('Contact/',Contact,name='Contact'),
    path('About/',About,name='About'),
    path('Vlab/<int:pk>/', Vlab, name='Vlab'),
    path('tinymce/', include('tinymce.urls')),
    path('delete/<int:pk>/', delete, name='delete'),
]



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
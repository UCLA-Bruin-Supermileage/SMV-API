"""smvDashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, reverse
from django.shortcuts import redirect
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

admin.site.enable_nav_sidebar = False
admin.site.site_header = 'SMV Admin Dashboard'
admin.site.site_title  =  "SMV Admin Dashboard"
admin.site.index_title  =  "Car Data"

def redirect_home(request):
    return redirect(reverse('dash_admin'))

urlpatterns = [
    # path('', redirect_home),
    path('admin/', admin.site.urls),
    path('', include('mqtt.urls')),
    path('apidocs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('apidocs/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('apidocs/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oidc/', include('mozilla_django_oidc.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('', include('comanage.urls')),
]

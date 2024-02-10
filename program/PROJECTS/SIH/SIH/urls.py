# SIH/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('credentialssss/', include('credentialssss.urls')),
    path('', include('credentialssss.urls')),  # Root URL includes credentialssss URLs
]

"""drwt URL Configuration."""
from django.urls import path, include

urlpatterns = [
    path('', include('drwt.leads.urls')),
]

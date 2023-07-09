from . import views
from django.urls import path, include


urlpatterns = [
    path('register/', views.register),
    path('', views.welcome),
    path('', include('django.contrib.auth.urls')),
]
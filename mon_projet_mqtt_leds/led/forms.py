from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('/led/', views.led),
    path('/config_ssid', views.ssid),
]
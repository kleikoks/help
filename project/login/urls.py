from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('privacy_policy/', privacy_policy, name='privacy_policy')
]

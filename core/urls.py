from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.urls')),
    path('', include('project.bot.urls')),
]


# allauth
urlpatterns += [
    path('accounts/', include('allauth.urls')),
]

from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.urls')),
    path('', include('project.bot.urls')),
    path('', include('project.login.urls')),
]


#SMS
urlpatterns += [
    path('', include('project.sms.urls')),
    path('task/', task, name='task'),
]

#OATUH

urlpatterns += [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('social-auth/', include('social_django.urls', namespace="social")),
]
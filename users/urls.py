from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import (
    home,
    login,
    add_profile

)

app_name = 'params'

urlpatterns = [
    path('', home, name='home'),
    #path('login', login, name='login'),
    path('add_profile', add_profile, name='add_profile'),
]
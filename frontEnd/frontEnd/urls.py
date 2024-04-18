
from django.contrib import admin
from django.urls import path
from frontApp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('dashh/', dashboard),
    path('register/', register)
]

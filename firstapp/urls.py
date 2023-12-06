from django.contrib import admin
from django.urls import path, include

from firstapp.views import index

urlpatterns = [
    path('', index)
]

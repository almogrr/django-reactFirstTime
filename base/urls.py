from django.contrib import admin
from . import views
from django.urls import path, include
from base.views import *
urlpatterns = [
    path('', views.index),
    path('react', reactview.as_view(),name="react"),
]
    

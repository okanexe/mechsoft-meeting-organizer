from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.current_meeting),
    path('add', views.add_meeting),
    path('update', views.update_meeting),
]
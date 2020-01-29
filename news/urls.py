from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('scrap/', views.web_scrap, name='scrap'),
    path('', views.newsList, name='newslist'),
]
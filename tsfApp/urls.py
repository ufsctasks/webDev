from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('eventos/', views.eventos, name='eventos'),
    path('guia/', views.guia, name='guia'),
    path('prj/', views.prj, name='prj'),
    path('voluntariado/', views.voluntariado, name='voluntariado'),
]

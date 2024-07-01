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
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('recovery/', views.recovery, name='recovery'),
    path('test_500_view/', views.test_500_view, name='test_500_view'),
    path('projetos/<int:projeto_id>/', views.projeto_detail, name='projetos_detail'),
]

handler404 = 'tsfApp.views.custom_404_view'

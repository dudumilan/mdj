from django.contrib import admin
from django.urls import path
from mcmusic.exposicoes import views


urlpatterns = [
    path('', views.home, name='home'),
    path('exposicoes/', views.exposicoes, name='exposicoes'),
    path('linha-do-tempo/', views.linha_do_tempo, name='linha_do_tempo'),
    path('visita-virtual/', views.visita_virtual, name='visita_virtual'),
    path('contato/', views.contato, name='contato'),
    path('exposicao/<int:id>/', views.detalhe, name='exposicao_detalhe'),
    path('jogo/<int:id>/', views.jogo_detalhe, name='jogo_detalhe'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contato', views.contato, name="contato"),
    path('contato2/<str:nome>', views.contato2, name="contato2"),
    path('pessoas/', views.lista_pessoas, name='lista_pessoas'),
    path('pessoas/<int:id>/', views.detalhe_pessoa, name='detalhe_pessoa'),

]

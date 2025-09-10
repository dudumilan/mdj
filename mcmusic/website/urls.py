from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contato/',views.contato,name='contato'),
    # path('dieta/', views.dieta, name='dieta'),
    # path('cronograma/', views.cronograma, name='cronograma'),
    # path('musculos/', views.musculos, name='musculos'),
    # path('cargas/', views.cargas, name='cargas'),

]



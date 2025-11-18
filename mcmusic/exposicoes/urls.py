from django.contrib import admin
from django.urls import path
from mcmusic.exposicoes import views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jogo/sonic/', views.sonic_intro, name='sonic_intro'),
    path('jogo/sonic/menu/', views.sonic_menu, name='sonic_menu'),
    path('jogo/sonic/historia/',views.sonic_historia, name='sonic_historia'),
    path('jogo/streetfighter2/', views.streetfighter2_intro, name='streetfighter2_intro'),
    path('jogo/streetfighter2/menu/', views.streetfighter2_menu, name='streetfighter2_menu'),
    path('jogo/streetfighter2/historia/', views.streetfighter2_historia, name='streetfighter2_historia'),
    path('jogo/<int:id>/', views.jogo_detalhe, name='jogo_detalhe'),
    path('jogo/<str:nome>/', views.jogo, name='jogo'),
    path('', views.home, name='home'),
    path('exposicoes/', views.exposicoes, name='exposicoes'),
    path('linha-do-tempo/', views.linha_do_tempo, name='linha_do_tempo'),
    path('visita-virtual/', views.visita_virtual, name='visita_virtual'),
    path('contato/', views.contato, name='contato'),
    path('exposicao/<int:id>/', views.detalhe, name='exposicao_detalhe'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
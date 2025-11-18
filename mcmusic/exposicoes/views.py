from django.shortcuts import render
from mcmusic.exposicoes.models import Slideshow
from django.shortcuts import render, get_object_or_404
from .models import Slideshow, Jogo
from django.http import HttpResponse

def jogo(request, nome):
    jogos = {
        "sonic": {"titulo": "Sonic", "template": "jogos/intro.html"},
    }
    info = jogos.get(nome)
    if not info:
        return HttpResponse("Jogo não encontrado")
    return render(request, info["template"], info)

def jogo_detalhe(request, id):
    jogo = get_object_or_404(Slideshow, id=id)
    return render(request, 'jogo_detalhe.html', {'jogo': jogo})

def streetfighter2_intro(request):
    return render(request, 'jogos/streetfighter2/intro.html')

def streetfighter2_menu(request):
    return render(request, 'jogos/streetfighter2/menu.html')


def home(request):
    slideshows = Slideshow.objects.all()
    print(slideshows)
    return render(request,'index.html',{'slideshows':slideshows})

def exposicoes(request):
    return render(request, 'exposicoes.html')

def linha_do_tempo(request):
    return render(request, 'linha_do_tempo.html')

def visita_virtual(request):
    return render(request, 'visita_virtual.html')

def contato(request):
    return render(request, 'contato.html')

def detalhe(request, id):
    slide = get_object_or_404(Slideshow, id=id)
    return render(request, 'detalhe.html', {'slide': slide})

def sonic_intro(request):
    return render(request, 'jogos/sonic/intro.html')

def sonic_menu(request):
    return render(request, 'jogos/sonic/menu.html')

def sonic_historia(request):
    return render(request, 'jogos/sonic/sonic_historia.html')

from django.shortcuts import render
from mcmusic.exposicoes.models import Slideshow
from django.shortcuts import render, get_object_or_404
from .models import Slideshow
from .models import Jogo



def jogo_detalhe(request, id):
    jogo = get_object_or_404(Slideshow, id=id)
    return render(request, 'jogo_detalhe.html', {'jogo': jogo})

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

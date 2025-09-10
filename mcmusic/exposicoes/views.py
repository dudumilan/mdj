from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def exposicoes(request):
    return render(request, 'exposicoes.html')

def linha_do_tempo(request):
    return render(request, 'linha_do_tempo.html')

def visita_virtual(request):
    return render(request, 'visita_virtual.html')

def contato(request):
    return render(request, 'contato.html')
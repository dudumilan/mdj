from django.shortcuts import render
from .models import Pessoa
# Create your views here.
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def contato(request):
    nome="Carlos"
    idade = "17"

    return render(request, 'contato.html', {'nome': nome, "idade": idade})

def lista_pessoas(request):
    pessoas = Pessoa.objects.all().order_by('nome')
    return render(request, 'pessoas.html', {'pessoas': pessoas})
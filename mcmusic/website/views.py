from django.shortcuts import render
from .models import Pessoa
# Create your views here.
def home(request):
    return render(request,'index.html')

def contato(request):
    nome="Carlos"
    idade = "17"

    return render(request, 'contato.html', {'nome': nome, "idade": idade})

def contato2(request, nome):    
    idade = "17"
    return render(request, 'contato.html', {'nome': nome, "idade": idade})

def contato(request):
    return render(request, 'contato.html')



def lista_pessoas(request):
    pessoas = Pessoa.objects.all().order_by('nome')
    return render(request, 'pessoas.html', {'pessoas': pessoas})
    

def detalhe_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    return render(request, 'pessoa_detalhe.html', {'pessoa': pessoa})


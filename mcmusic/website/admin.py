from django.contrib import admin
from mcmusic.website.models import Pessoa
# Register your models here.

class PessoaModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'telefone', 'data_nascimento')


admin.site.register(Pessoa, PessoaModelAdmin)
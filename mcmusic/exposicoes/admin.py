from django.contrib import admin
from mcmusic.exposicoes.models import Pessoa
from exposicoes.models import Slideshow
# Register your models here.

class SlideshowModelAdmin(admin.ModelAdmin):
    list_display = ['titulo','imagem','alt','descricao',]
    search_fields = ('titulo',)


admin.site.register(Slideshow,SlideshowModelAdmin)

class PessoaModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'telefone', 'data_nascimento', 'criado_em')
    list_filter = ('criado_em', 'atualizado_em')
    search_fields = ('nome', 'email', 'cpf', 'telefone')
    ordering = ('nome',)
    readonly_fields = ('criado_em', 'atualizado_em')
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('nome', 'email', 'cpf', 'data_nascimento', 'telefone',)
        }),
        ('Timestamps', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',),
        }),
    )

admin.site.register(Pessoa, PessoaModelAdmin)
#admin.site.register(Pessoa)

admin.site.site_header = "Administração Geral - dudumilan"
admin.site.site_title = "Administração do Site"
from django.db import models
from django.utils.text import slugify

class Slideshow(models.Model):
    titulo = models.CharField(max_length=255, blank=True, null=True, default="Sem título")
    slug = models.SlugField(unique=True, blank=True, null=True, default="default-slideshow")
    imagem = models.ImageField(verbose_name="Imagem", upload_to='slideshow/')
    alt = models.CharField(verbose_name="Alternative", max_length=100, blank=True, null=True)
    descricao = models.TextField("Descrição", blank=True, null=True)

    class Meta:
        verbose_name_plural = 'SlideShow'
        verbose_name = 'SlideShow'
        ordering = ('titulo',)

    def __str__(self):
        return self.titulo or "Sem título"

    def save(self, *args, **kwargs):
        if not self.slug and self.titulo:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)


class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    lancamento = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    endereco = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

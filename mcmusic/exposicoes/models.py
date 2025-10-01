from django.db import models


# Create your models here.

class Slideshow(models.Model):
    imagem = models.ImageField(verbose_name ="Imagem", upload_to='slideshow/')
    titulo = models.CharField(verbose_name ="titulo",max_length=50, blank=True, null=True,)
    alt = models.CharField(verbose_name ="Alternative",max_length=100, blank=True, null=True,)
    descricao = models.TextField("Descrição",  blank=True, null= True)

    class Meta:
        verbose_name_plural = 'SlideShow'
        verbose_name = 'SlideShow'
        ordering = ('titulo',)

    def __str__(self):
        return self.titulo

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True)  # Ex: 000.000.000-00
    telefone = models.CharField(max_length=20, blank=True)
    endereco = models.TextField(blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
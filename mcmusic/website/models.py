from django.db import models

# Create your models here.

class Pessoa(models.Model):
        nome = models.CharField(max_length=100)
        email = models.EmailField(unique=True)
        data_nascimento = models.DateField(null=True, blank=True)
        cpf = models.CharField(max_length=14, unique=True)
        telefone = models.CharField(max_length=20, blank=True)


        def __str__(self) -> str:
            return self.nome
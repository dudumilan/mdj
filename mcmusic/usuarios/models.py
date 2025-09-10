from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Campos adicionais, se quiser
    apelido = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(
        upload_to="avatar/",   # pasta dentro de MEDIA_ROOT
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username

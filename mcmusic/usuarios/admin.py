from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    # Garante que o campo extra (bio) apareça
    fieldsets = UserAdmin.fieldsets + (
        ("Informações adicionais", {"fields": ("bio",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Informações adicionais", {"fields": ("bio",)}),
    )
    
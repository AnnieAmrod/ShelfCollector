from django.contrib import admin

# Register your models here.
from .models import Usuario


class UsuarioAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('email', 'nombre', 'is_superuser')
    search_fields = ['email', 'nombre']


admin.site.register(Usuario, UsuarioAdmin)

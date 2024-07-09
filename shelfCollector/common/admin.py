from django.contrib import admin

# Register your models here.
from .models import Genero, Carpeta


class GeneroAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['nombre', 'descripcion']


class CarpetaAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['nombre', 'descripcion']


admin.site.register(Genero, GeneroAdmin)
admin.site.register(Carpeta, CarpetaAdmin)

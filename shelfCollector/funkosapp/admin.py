from django.contrib import admin

# Register your models here.
from .models import (Coleccion, Tamano, Tipo, Funko)


class ColeccionAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['nombre', 'descripcion', 'url']


class TamanoAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['nombre', 'descripcion']


class TipoAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['nombre', 'descripcion']


class FunkoAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['n_coleccion', 'nombre', 'img', 'display_coleccion', 'serie', 'display_tamano',
                                        'display_tipo', 'display_genero', 'num_serie', 'wish_list', 'display_carpeta']

    def display_coleccion(self, obj):
        return ", ".join([coleccion.nombre for coleccion in obj.coleccion.all()])

    display_coleccion.short_description = 'Colección'

    def display_tamano(self, obj):
        return ", ".join([tamano.nombre for tamano in obj.tamano.all()])

    display_tamano.short_description = 'Tamaño'

    def display_tipo(self, obj):
        return ", ".join([tipo.nombre for tipo in obj.tipo.all()])

    display_tipo.short_description = 'Tipo'

    def display_genero(self, obj):
        return ", ".join([genero.nombre for genero in obj.genero.all()])

    display_genero.short_description = 'Género'

    def display_carpeta(self, obj):
        return ", ".join([carpeta.nombre for carpeta in obj.carpeta.all()])

    display_carpeta.short_description = 'Tipo'


admin.site.register(Coleccion, ColeccionAdmin)
admin.site.register(Tamano, TamanoAdmin)
admin.site.register(Tipo, TipoAdmin)
admin.site.register(Funko, FunkoAdmin)

from django.contrib import admin
from django.utils.html import format_html
from django.utils.text import Truncator

# Register your models here.
from .models import (Distibuidor, Desarrollador, Modo, Plataforma, EdadRecomendada,
                     TipoContenido, Coleccion, Programa, Videojuego, Recopilacion)


class DistibuidorAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['nombre', 'descripcion']


class DesarrolladorAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['nombre', 'descripcion']


class ModoAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['modo_juego']


class PlataformaAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['nombre', 'retrocompatible']


class EdadRecomendadaAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['numero', 'color', 'descripcion']


class TipoContenidoAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['nombre']


class ColeccionAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['nombre', 'descripcion', 'url']


class ProgramaAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['nombre', 'descripcion']


class VideojuegoAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['nombre', 'display_descripcion', 'display_sinopsis', 'anio', 'img', 'display_distribuidores',
                    'display_desarrolladores', 'display_modos_juego', 'display_generos',
                    'display_plataformas', 'precio', 'display_edad_recomendada',
                    'display_tipo_contenido', 'tenemos', 'wish_list', 'display_coleccion',
                    'formato', 'display_programa', 'display_carpetas']

    def display_descripcion(self, obj):
        truncated_text = Truncator(obj.descripcion).chars(60)
        return format_html(truncated_text)

    display_descripcion.short_description = 'Sinopsis'

    def display_sinopsis(self, obj):
        truncated_text = Truncator(obj.sinopsis).chars(60)
        return format_html(truncated_text)

    display_sinopsis.short_description = 'Sinopsis'

    def display_distribuidores(self, obj):
        return ", ".join([distribuidor.nombre for distribuidor in obj.distribuidor.all()])

    display_distribuidores.short_description = 'Distribuidores'

    def display_desarrolladores(self, obj):
        return ", ".join([desarrollador.nombre for desarrollador in obj.desarrollador.all()])

    display_desarrolladores.short_description = 'Desarrolladores'

    def display_modos_juego(self, obj):
        return ", ".join([modo.modo_juego for modo in obj.modo_juego.all()])

    display_modos_juego.short_description = 'Modos de Juego'

    def display_generos(self, obj):
        return ", ".join([genero.nombre for genero in obj.genero.all()])

    display_generos.short_description = 'Géneros'

    def display_plataformas(self, obj):
        return ", ".join([plataforma.nombre for plataforma in obj.plataforma.all()])

    display_plataformas.short_description = 'Plataformas'

    def display_edad_recomendada(self, obj):
        return f"PEGI {obj.edad_recomendada.numero} ({obj.edad_recomendada.color}) {obj.edad_recomendada.descripcion}"

    display_edad_recomendada.short_description = 'Edad Recomendada'

    def display_tipo_contenido(self, obj):
        return ", ".join([tipo_contenido.nombre for tipo_contenido in obj.tipo_contenido.all()])

    display_tipo_contenido.short_description = 'Tipo de Contenido'

    def display_coleccion(self, obj):
        if obj.coleccion:
            return obj.coleccion.nombre
        return "--"

    display_coleccion.short_description = 'Colección'

    def display_programa(self, obj):
        return ", ".join([programa.nombre for programa in obj.programa.all()])

    display_programa.short_description = 'Programa'

    def display_carpetas(self, obj):
        return ", ".join([carpetas.nombre for carpetas in obj.carpeta.all()])

    display_carpetas.short_description = 'Carpetas'


class RecopilacionAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['nombre', 'descripcion', 'display_videojuegos']

    def display_videojuegos(self, obj):
        return ", ".join([videojuego.nombre for videojuego in obj.videojuegos.all()])

    display_videojuegos.short_description = 'Videojuegos'


admin.site.register(Distibuidor, DistibuidorAdmin)
admin.site.register(Desarrollador, DesarrolladorAdmin)
admin.site.register(Modo, ModoAdmin)
admin.site.register(Plataforma, PlataformaAdmin)
admin.site.register(EdadRecomendada, EdadRecomendadaAdmin)
admin.site.register(TipoContenido, TipoContenidoAdmin)
admin.site.register(Coleccion, ColeccionAdmin)
admin.site.register(Programa, ProgramaAdmin)
admin.site.register(Videojuego, VideojuegoAdmin)
admin.site.register(Recopilacion, RecopilacionAdmin)

from django.contrib import admin

# Register your models here.
from .models import (Autor, Editorial, Idioma, Libro)


class AutorAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['nombre', 'biografia', 'url']


class EditorialAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['nombre', 'direccion', 'url']


class IdiomaAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['nombre']


class LibroAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['titulo', 'descripcion', 'fecha_publicacion', 'portada', 'display_autor',
                                        'display_genero', 'display_editorial', 'isbn', 'fecha_leido', 'leido_por',
                                        'precio', 'paginas', 'display_idioma', 'display_carpetas', 'tenemos', 'wish_list']

    def display_autor(self, obj):
        return ", ".join([autor.nombre for autor in obj.autor.all()])

    display_autor.short_description = 'Autor'

    def display_genero(self, obj):
        return ", ".join([genero.nombre for genero in obj.genero.all()])

    display_genero.short_description = 'Genero'

    def display_editorial(self, obj):
        return ", ".join([editorial.nombre for editorial in obj.editorial.all()])

    display_editorial.short_description = 'Editorial'

    def display_idioma(self, obj):
        return ", ".join([idioma.nombre for idioma in obj.idioma.all()])

    display_idioma.short_description = 'Idioma'

    def display_carpetas(self, obj):
        return ", ".join([carpetas.nombre for carpetas in obj.carpeta.all()])

    display_carpetas.short_description = 'Carpetas'


admin.site.register(Autor, AutorAdmin)
admin.site.register(Editorial, EditorialAdmin)
admin.site.register(Idioma, IdiomaAdmin)
admin.site.register(Libro, LibroAdmin)

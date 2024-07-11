from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Autor, Editorial, Idioma, Libro


# Create your views here.
class AutorCreateView(CreateView):
    model = Autor
    fields = ['nombre', 'biografia', 'url']


class EditorialCreateView(CreateView):
    model = Editorial
    fields = ['nombre', 'direccion', 'url']


class IdiomaCreateView(CreateView):
    model = Idioma
    fields = ['nombre']


class LibroCreateView(CreateView):
    model = Libro
    fields = ['titulo', 'descripcion', 'fecha_publicacion', 'portada', 'autor', 'genero', 'editorial', 'isbn',
              'fecha_leido', 'leido_por', 'precio', 'paginas', 'idioma', 'carpeta', 'tenemos', 'wish_list']

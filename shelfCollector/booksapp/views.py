from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Autor, Editorial, Idioma, Libro
from common.mixins import AreaRestringidaMixin


# Create your views here.
class AutorCreateView(AreaRestringidaMixin, CreateView):
    model = Autor
    fields = ['nombre', 'biografia', 'url']


class EditorialCreateView(AreaRestringidaMixin, CreateView):
    model = Editorial
    fields = ['nombre', 'direccion', 'url']


class IdiomaCreateView(AreaRestringidaMixin, CreateView):
    model = Idioma
    fields = ['nombre']


class LibroCreateView(AreaRestringidaMixin, CreateView):
    model = Libro
    fields = ['titulo', 'descripcion', 'fecha_publicacion', 'portada', 'autor', 'genero', 'editorial', 'isbn',
              'fecha_leido', 'leido_por', 'precio', 'paginas', 'idioma', 'carpeta', 'tenemos', 'wish_list']

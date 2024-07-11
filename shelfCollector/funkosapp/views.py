from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Coleccion, Tamano, Tipo, Funko


# Create your views here.
class ColeccionCreateView(CreateView):
    model = Coleccion
    fields = ['nombre', 'descripcion', 'url']


class TamanoCreateView(CreateView):
    model = Tamano
    fields = ['nombre', 'descripcion']


class TipoCreateView(CreateView):
    model = Tipo
    fields = ['nombre', 'descripcion']


class FunkoCreateView(CreateView):
    model = Funko
    fields = ['n_coleccion', 'nombre', 'img', 'coleccion', 'serie', 'tamano', 'tipo', 'genero',
              'num_serie', 'tenemos', 'wish_list', 'carpeta']

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Genero, Carpeta


# Create your views here.
class HomeView(TemplateView):
    template_name = 'common/home.html'


# CRUD
class GeneroCreateView(CreateView):
    model = Genero
    fields = ['nombre', 'descripcion']


class CarpetaCreateView(CreateView):
    model = Carpeta
    fields = ['nombre', 'descripcion']

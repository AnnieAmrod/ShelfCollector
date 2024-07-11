from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import (Distibuidor, Desarrollador, Plataforma, EdadRecomendada, TipoContenido, Coleccion,
                     Programa, Videojuego, Recopilacion)
from .mixins import DistribuidorMixin


# Create your views here.
class DistribuidorCreateView(DistribuidorMixin, SuccessMessageMixin, CreateView):
    # model = Distibuidor
    # fields = ['nombre', 'descripcion']
    # success_url = reverse_lazy('distribuidor_list')

    # def get_success_url(self):
    #     object = self.object
    #     return reverse_lazy('distribuidor_update', kwargs={'pk': object.id})

    success_message = "Distribuidor creado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class DistribuidorUpdateView(DistribuidorMixin, SuccessMessageMixin, UpdateView):
    model = Distibuidor
    # fields = ['nombre', 'descripcion']
    # success_url = reverse_lazy('distribuidor_list')

    # def get_success_url(self):
    #     object = self.object
    #     return reverse_lazy('distribuidor_update', kwargs={'pk': object.id})

    success_message = "Distribuidor editado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class DistribuidorDeleteView(DeleteView):
    model = Distibuidor
    success_url = reverse_lazy('distribuidor')
    template_name = 'gamesapp/distribuidor_confirm_delete.html'


class DesarrolladorCreateView(CreateView):
    model = Desarrollador
    fields = ['nombre', 'descripcion']


class ModoCreateView(CreateView):
    model = Desarrollador
    fields = ['modo_juego']


class PlataformaCreateView(CreateView):
    model = Plataforma
    fields = ['nombre', 'retrocompatible']


class EdadRecomendadaCreateView(CreateView):
    model = EdadRecomendada
    fields = ['numero', 'color', 'descripcion']


class TipoContenidoCreateView(CreateView):
    model = TipoContenido
    fields = ['nombre']


class ColeccionCreateView(CreateView):
    model = Coleccion
    fields = ['nombre', 'descripcion', 'url']


class ProgramaCreateView(CreateView):
    model = Programa
    fields = ['nombre', 'descripcion']


class VideojuegoCreateView(CreateView):
    model = Videojuego
    fields = ['nombre', 'descripcion', 'sinopsis', 'anio', 'img', 'distribuidor', 'desarrollador', 'modo_juego',
              'genero', 'plataforma', 'precio', 'edad_recomendada', 'tipo_contenido', 'tenemos', 'wish_list',
              'coleccion', 'formato', 'programa', 'carpeta']


class RecopilacionCreateView(CreateView):
    model = Recopilacion
    fields = ['nombre', 'descripcion', 'videojuegos']

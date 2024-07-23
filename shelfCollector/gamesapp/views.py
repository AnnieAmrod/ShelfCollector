from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import (Distibuidor, Desarrollador, Modo, Plataforma, EdadRecomendada, TipoContenido, Coleccion,
                     Programa, Videojuego, Recopilacion)
from .mixins import DistribuidorMixin, DesarrolladorMixin


# Distribuidor ************************************************************************************************
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


# Desarrollador ***********************************************************************************************
class DesarrolladorCreateView(DesarrolladorMixin, SuccessMessageMixin, CreateView):
    # model = Desarrollador
    # fields = ['nombre', 'descripcion']

    success_message = "Desarrollador creado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class DesarrolladorUpdateView(DesarrolladorMixin, SuccessMessageMixin, UpdateView):
    # model = Desarrollador
    # fields = ['nombre', 'descripcion']

    success_message = "Desarrollador editado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class DesarrolladorDeleteView(DeleteView):
    model = Desarrollador
    success_url = reverse_lazy('desarrollador')
    template_name = 'gamesapp/desarrollador_confirm_delete.html'


# Modo de juego ************************************************************************************************
class ModoCreateView(CreateView):
    model = Modo
    fields = ['modo_juego']


# Plataforma ***************************************************************************************************
class PlataformaCreateView(CreateView):
    model = Plataforma
    fields = ['nombre', 'retrocompatible']


# Edad Recomendada *********************************************************************************************
class EdadRecomendadaCreateView(CreateView):
    model = EdadRecomendada
    fields = ['numero', 'color', 'descripcion']


# Tipo de Contenido *********************************************************************************************
class TipoContenidoCreateView(CreateView):
    model = TipoContenido
    fields = ['nombre']


# Colección *****************************************************************************************************
class ColeccionCreateView(CreateView):
    model = Coleccion
    fields = ['nombre', 'descripcion', 'url']


# Programa ******************************************************************************************************
class ProgramaCreateView(CreateView):
    model = Programa
    fields = ['nombre', 'descripcion']


# Videojuego ****************************************************************************************************
class VideojuegoCreateView(CreateView):
    model = Videojuego
    fields = ['nombre', 'descripcion', 'sinopsis', 'anio', 'img', 'distribuidor', 'desarrollador', 'modo_juego',
              'genero', 'plataforma', 'precio', 'edad_recomendada', 'tipo_contenido', 'tenemos', 'wish_list',
              'coleccion', 'formato', 'programa', 'carpeta']


# Recopilación **************************************************************************************************
class RecopilacionCreateView(CreateView):
    model = Recopilacion
    fields = ['nombre', 'descripcion', 'videojuegos']

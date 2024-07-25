from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import (Distibuidor, Desarrollador, Modo, Plataforma, EdadRecomendada, TipoContenido, Coleccion,
                     Programa, Videojuego, Recopilacion)
from .mixins import (DistribuidorMixin, DesarrolladorMixin, ModoMixin, PlataformaMixin, EdadRecomendadaMixin,
                     TipoContenidoMixin, ColeccionMixin, ProgramaMixin, VideojuegoMixin)


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
    model = Desarrollador

    success_message = "Desarrollador editado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class DesarrolladorDeleteView(DeleteView):
    model = Desarrollador
    success_url = reverse_lazy('desarrollador')
    template_name = 'gamesapp/desarrollador_confirm_delete.html'


# Modo de juego ************************************************************************************************
class ModoCreateView(ModoMixin, SuccessMessageMixin, CreateView):
    # model = Modo
    # fields = ['modo_juego']

    success_message = "Modo de juego creado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class ModoUpdateView(ModoMixin, SuccessMessageMixin, UpdateView):
    model = Modo

    success_message = "Modo de juego editado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class ModoDeleteView(DeleteView):
    model = Modo
    success_url = reverse_lazy('modo')
    template_name = 'gamesapp/modo_confirm_delete.html'


# Plataforma ***************************************************************************************************
class PlataformaCreateView(PlataformaMixin, SuccessMessageMixin, CreateView):
    # model = Plataforma
    # fields = ['nombre', 'retrocompatible']

    success_message = "Plataforma creada exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class PlataformaUpdateView(PlataformaMixin, SuccessMessageMixin, UpdateView):
    model = Plataforma

    success_message = "Plataforma editada exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class PlataformaDeleteView(DeleteView):
    model = Plataforma
    success_url = reverse_lazy('plataforma')
    template_name = 'gamesapp/plataforma_confirm_delete.html'


# Edad Recomendada *********************************************************************************************
class EdadRecomendadaCreateView(EdadRecomendadaMixin, SuccessMessageMixin, CreateView):
    # model = EdadRecomendada
    # fields = ['numero', 'color', 'descripcion']

    success_message = "Edad Recomendada creada exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class EdadRecomendadaUpdateView(EdadRecomendadaMixin, SuccessMessageMixin, UpdateView):
    model = EdadRecomendada

    success_message = "Edad Recomendada editada exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class EdadRecomendadaDeleteView(DeleteView):
    model = EdadRecomendada
    success_url = reverse_lazy('edad_recomendada')
    template_name = 'gamesapp/edad_recomendada_confirm_delete.html'


# Tipo de Contenido *********************************************************************************************
class TipoContenidoCreateView(TipoContenidoMixin, SuccessMessageMixin, CreateView):
    # model = TipoContenido
    # fields = ['nombre']

    success_message = "Tipo de contenido creado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class TipoContenidoUpdateView(TipoContenidoMixin, SuccessMessageMixin, UpdateView):
    model = TipoContenido

    success_message = "Tipo de contenido editado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class TipoContenidoDeleteView(DeleteView):
    model = TipoContenido
    success_url = reverse_lazy('tipo_contenido')
    template_name = 'gamesapp/tipo_contenido_confirm_delete.html'


# Colección *****************************************************************************************************
class ColeccionCreateView(ColeccionMixin, SuccessMessageMixin, CreateView):
    # model = Coleccion
    # fields = ['nombre', 'descripcion', 'url']

    success_message = "Colección creada exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class ColeccionUpdateView(ColeccionMixin, SuccessMessageMixin, UpdateView):
    model = Coleccion

    success_message = "Colección editada exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class ColeccionDeleteView(DeleteView):
    model = Coleccion
    success_url = reverse_lazy('coleccion')
    template_name = 'gamesapp/coleccion_confirm_delete.html'


# Programa ******************************************************************************************************
class ProgramaCreateView(ProgramaMixin, SuccessMessageMixin, CreateView):
    # model = Programa
    # fields = ['nombre', 'descripcion']

    success_message = "Programa creado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class ProgramaUpdateView(ProgramaMixin, SuccessMessageMixin, UpdateView):
    model = Programa

    success_message = "Programa editado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class ProgramaDeleteView(DeleteView):
    model = Programa
    success_url = reverse_lazy('programa')
    template_name = 'gamesapp/programa_confirm_delete.html'


# Videojuego ****************************************************************************************************
class VideojuegoCreateView(VideojuegoMixin, SuccessMessageMixin, CreateView):
    # model = Videojuego
    # fields = ['nombre', 'descripcion', 'sinopsis', 'anio', 'img', 'distribuidor', 'desarrollador', 'modo_juego',
    #           'genero', 'plataforma', 'precio', 'edad_recomendada', 'tipo_contenido', 'tenemos', 'wish_list',
    #           'coleccion', 'formato', 'programa', 'carpeta']

    success_message = "Videojuego creado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class VideojuegoUpdateView(VideojuegoMixin, SuccessMessageMixin, UpdateView):
    model = Videojuego

    success_message = "Videojuego editado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class VideojuegoDeleteView(DeleteView):
    model = Videojuego
    success_url = reverse_lazy('videojuego')
    template_name = 'gamesapp/videojuego_confirm_delete.html'


# Recopilación **************************************************************************************************
class RecopilacionCreateView(CreateView):
    model = Recopilacion
    fields = ['nombre', 'descripcion', 'videojuegos']

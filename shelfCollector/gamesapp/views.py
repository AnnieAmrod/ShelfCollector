from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView

from .models import (Distibuidor, Desarrollador, Modo, Plataforma, EdadRecomendada, TipoContenido, Coleccion,
                     Programa, Videojuego, Recopilacion)
from .mixins import (DistribuidorMixin, DesarrolladorMixin, ModoMixin, PlataformaMixin, EdadRecomendadaMixin,
                     TipoContenidoMixin, ColeccionMixin, ProgramaMixin, VideojuegoMixin, RecopilacionMixin)


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


class VideojuegoListView(TemplateView):
    template_name = 'gamesapp/listado_videojuegos.html'

    def get_context_data(self, **kwargs):
        context = super(VideojuegoListView, self).get_context_data(**kwargs)

        # Obtener los valores de los filtros enviados por el usuario
        nombre = self.request.GET.get('nombre')
        anio = self.request.GET.get('anio')

        # Sacar más de un registro al filtrar
        distribuidor_id = kwargs.get('distribuidor_id')
        desarrollador_id = kwargs.get('desarrollador_id')
        modo_juego_id = kwargs.get('modo_juego_id')
        genero_id = kwargs.get('genero_id')
        plataforma_id = kwargs.get('plataforma_id')
        coleccion_id = kwargs.get('coleccion_id')
        carpeta_id = kwargs.get('carpeta_id')


        # Obtener todos los videojuegos
        videojuegos = Videojuego.objects.all()

        # Filtrar los objetos de Videojuego utilizando los filtros recibidos

        if nombre:
            # Filtrar por nombre escrito
            videojuegos = videojuegos.filter(nombre__icontains=nombre)

        if anio:
            # Filtrar por año escrito
            videojuegos = videojuegos.filter(anio__icontains=anio)

        if distribuidor_id:
            # Filtrar por distribuidor seleccionado
            videojuegos = videojuegos.filter(distribuidor_id=distribuidor_id)

        if desarrollador_id:
            # Filtrar por desarrollador seleccionado
            videojuegos = videojuegos.filter(desarrollador_id=desarrollador_id)

        if modo_juego_id:
            # Filtrar por modo de juego seleccionado
            videojuegos = videojuegos.filter(modo_juego_id=modo_juego_id)

        if genero_id:
            # Filtrar por genero seleccionado
            videojuegos = videojuegos.filter(genero_id=genero_id)

        if plataforma_id:
            # Filtrar por plataforma seleccionada
            videojuegos = videojuegos.filter(plataforma_id=plataforma_id)

        if coleccion_id:
            # Filtrar por colección seleccionada
            videojuegos = videojuegos.filter(coleccion_id=coleccion_id)

        if carpeta_id:
            # Filtrar por carpeta seleccionada
            videojuegos = videojuegos.filter(carpeta_id=carpeta_id)

        # Obtener todos los videojuegos filtrados
        context['videojuego'] = videojuegos

        return context


# -------------------------------- Recuperar videojuego al clickar en un videojuego de Panel
def videojuego_detail_view(request,pk):
    videojuego = Videojuego.objects.get(pk=pk)
    context = {'videojuego': videojuego}
    return render(request,'gamesapp/detalle_videojuego.html',context)


# -------------------------------- Incluir código para que no explote la aplicación cuando se introduzca un id no válido.
    # -------------------------------- Que devuelva la página 404 o el objeto
def videojuegoView(request, pk):
    videojuego = get_object_or_404(Videojuego, pk=pk)
    context = {'videojuego': videojuego}
    return render(request, 'gamesapp/listado_videojuegos.html', context)


class VideojuegoDetailView(TemplateView):
    template_name = "gamesapp/detalle_videojuego.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        lost_id = kwargs.get('id')
        context['videojuego'] = Videojuego.objects.get(id=lost_id)
        return context





# Recopilación **************************************************************************************************
class RecopilacionCreateView(RecopilacionMixin, SuccessMessageMixin, CreateView):
    # model = Recopilacion
    # fields = ['nombre', 'descripcion', 'sinopsis', 'anio', 'img', 'distribuidor', 'desarrollador', 'modo_juego',
    #           'genero', 'plataforma', 'precio', 'edad_recomendada', 'tipo_contenido', 'tenemos', 'wish_list',
    #           'coleccion', 'formato', 'programa', 'carpeta', 'videojuegos']

    success_message = "Recopilación creada exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class RecopilacionUpdateView(RecopilacionMixin, SuccessMessageMixin, UpdateView):
    model = Recopilacion

    success_message = "Recopilación editada exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class RecopilacionDeleteView(DeleteView):
    model = Recopilacion
    success_url = reverse_lazy('recopilacion')
    template_name = 'gamesapp/recopilacion_confirm_delete.html'

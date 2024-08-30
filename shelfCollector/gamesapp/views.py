from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.db import transaction

from django.db.models import Count, Min

from .models import (Distibuidor, Desarrollador, Modo, Plataforma, EdadRecomendada, TipoContenido, Coleccion,
                     Programa, Videojuego, Recopilacion, Carpeta)
from .mixins import (DistribuidorMixin, DesarrolladorMixin, ModoMixin, PlataformaMixin, EdadRecomendadaMixin,
                     TipoContenidoMixin, ColeccionMixin, ProgramaMixin, VideojuegoMixin, RecopilacionMixin)
from common.mixins import AreaRestringidaMixin


# Distribuidor ************************************************************************************************
class DistribuidorCreateView(AreaRestringidaMixin, DistribuidorMixin, SuccessMessageMixin, CreateView):
    # model = Distibuidor
    # fields = ['nombre', 'descripcion']
    # success_url = reverse_lazy('distribuidor_list')

    # def get_success_url(self):
    #     object = self.object
    #     return reverse_lazy('distribuidor_update', kwargs={'pk': object.id})

    success_message = "Distribuidor creado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class DistribuidorUpdateView(AreaRestringidaMixin, DistribuidorMixin, SuccessMessageMixin, UpdateView):
    model = Distibuidor
    # fields = ['nombre', 'descripcion']
    # success_url = reverse_lazy('distribuidor_list')

    # def get_success_url(self):
    #     object = self.object
    #     return reverse_lazy('distribuidor_update', kwargs={'pk': object.id})

    success_message = "Distribuidor editado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class DistribuidorDeleteView(AreaRestringidaMixin, DeleteView):
    model = Distibuidor
    success_url = reverse_lazy('distribuidor')
    template_name = 'gamesapp/distribuidor_confirm_delete.html'


# Desarrollador ***********************************************************************************************
class DesarrolladorCreateView(AreaRestringidaMixin, DesarrolladorMixin, SuccessMessageMixin, CreateView):
    # model = Desarrollador
    # fields = ['nombre', 'descripcion']

    success_message = "Desarrollador creado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class DesarrolladorUpdateView(AreaRestringidaMixin, DesarrolladorMixin, SuccessMessageMixin, UpdateView):
    model = Desarrollador

    success_message = "Desarrollador editado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class DesarrolladorDeleteView(AreaRestringidaMixin, DeleteView):
    model = Desarrollador
    success_url = reverse_lazy('desarrollador')
    template_name = 'gamesapp/desarrollador_confirm_delete.html'


# Modo de juego ************************************************************************************************
class ModoCreateView(AreaRestringidaMixin, ModoMixin, SuccessMessageMixin, CreateView):
    # model = Modo
    # fields = ['modo_juego']

    success_message = "Modo de juego creado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class ModoUpdateView(AreaRestringidaMixin, ModoMixin, SuccessMessageMixin, UpdateView):
    model = Modo

    success_message = "Modo de juego editado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class ModoDeleteView(AreaRestringidaMixin, DeleteView):
    model = Modo
    success_url = reverse_lazy('modo')
    template_name = 'gamesapp/modo_confirm_delete.html'


# Plataforma ***************************************************************************************************
class PlataformaCreateView(AreaRestringidaMixin, PlataformaMixin, SuccessMessageMixin, CreateView):
    # model = Plataforma
    # fields = ['nombre', 'retrocompatible']

    success_message = "Plataforma creada exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class PlataformaUpdateView(AreaRestringidaMixin, PlataformaMixin, SuccessMessageMixin, UpdateView):
    model = Plataforma

    success_message = "Plataforma editada exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class PlataformaDeleteView(AreaRestringidaMixin, DeleteView):
    model = Plataforma
    success_url = reverse_lazy('plataforma')
    template_name = 'gamesapp/plataforma_confirm_delete.html'


# Edad Recomendada *********************************************************************************************
class EdadRecomendadaCreateView(AreaRestringidaMixin, EdadRecomendadaMixin, SuccessMessageMixin, CreateView):
    # model = EdadRecomendada
    # fields = ['numero', 'color', 'descripcion']

    success_message = "Edad Recomendada creada exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class EdadRecomendadaUpdateView(AreaRestringidaMixin, EdadRecomendadaMixin, SuccessMessageMixin, UpdateView):
    model = EdadRecomendada

    success_message = "Edad Recomendada editada exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class EdadRecomendadaDeleteView(AreaRestringidaMixin, DeleteView):
    model = EdadRecomendada
    success_url = reverse_lazy('edad_recomendada')
    template_name = 'gamesapp/edad_recomendada_confirm_delete.html'


# Tipo de Contenido *********************************************************************************************
class TipoContenidoCreateView(AreaRestringidaMixin, TipoContenidoMixin, SuccessMessageMixin, CreateView):
    # model = TipoContenido
    # fields = ['nombre']

    success_message = "Tipo de contenido creado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class TipoContenidoUpdateView(AreaRestringidaMixin, TipoContenidoMixin, SuccessMessageMixin, UpdateView):
    model = TipoContenido

    success_message = "Tipo de contenido editado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class TipoContenidoDeleteView(AreaRestringidaMixin, DeleteView):
    model = TipoContenido
    success_url = reverse_lazy('tipo_contenido')
    template_name = 'gamesapp/tipo_contenido_confirm_delete.html'


# Colección *****************************************************************************************************
class ColeccionCreateView(AreaRestringidaMixin, ColeccionMixin, SuccessMessageMixin, CreateView):
    # model = Coleccion
    # fields = ['nombre', 'descripcion', 'url']

    success_message = "Colección creada exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class ColeccionUpdateView(AreaRestringidaMixin, ColeccionMixin, SuccessMessageMixin, UpdateView):
    model = Coleccion

    success_message = "Colección editada exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class ColeccionDeleteView(AreaRestringidaMixin, DeleteView):
    model = Coleccion
    success_url = reverse_lazy('coleccion')
    template_name = 'gamesapp/coleccion_confirm_delete.html'


# Programa ******************************************************************************************************
class ProgramaCreateView(AreaRestringidaMixin, ProgramaMixin, SuccessMessageMixin, CreateView):
    # model = Programa
    # fields = ['nombre', 'descripcion']

    success_message = "Programa creado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class ProgramaUpdateView(AreaRestringidaMixin, ProgramaMixin, SuccessMessageMixin, UpdateView):
    model = Programa

    success_message = "Programa editado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class ProgramaDeleteView(AreaRestringidaMixin, DeleteView):
    model = Programa
    success_url = reverse_lazy('programa')
    template_name = 'gamesapp/programa_confirm_delete.html'


# Videojuego ****************************************************************************************************
class VideojuegoCreateView(AreaRestringidaMixin, VideojuegoMixin, SuccessMessageMixin, CreateView):
    # model = Videojuego
    # fields = ['nombre', 'descripcion', 'sinopsis', 'anio', 'img', 'distribuidor', 'desarrollador', 'modo_juego',
    #           'genero', 'plataforma', 'precio', 'edad_recomendada', 'tipo_contenido', 'tenemos', 'wish_list',
    #           'coleccion', 'formato', 'programa', 'carpeta']

    success_message = "Videojuego creado exitosamente"

    def form_valid(self, form):
        # Obtener el usuario actual
        user = self.request.user

        # Asignar el usuario actual al campo 'usuario' del formulario
        form.instance.usuario = user

        # Verificar si ya existe un videojuego con el mismo nombre y usuario
        if Videojuego.objects.filter(nombre=form.cleaned_data['nombre'],
                                     anio=form.cleaned_data['anio'],
                                     usuario=user).exists():
            form.add_error('nombre', 'Ya existe un videojuego con este nombre y año para tu cuenta.')
            return self.form_invalid(form)

        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Verificar si hay carpetas disponibles en la base de datos
        context['hay_carpetas'] = Carpeta.objects.exists()

        return context


class VideojuegoUpdateView(AreaRestringidaMixin, VideojuegoMixin, SuccessMessageMixin, UpdateView):
    model = Videojuego

    success_message = "Videojuego editado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Verificar si hay carpetas disponibles en la base de datos
        context['hay_carpetas'] = Carpeta.objects.exists()

        return context


class VideojuegoDeleteView(AreaRestringidaMixin, DeleteView):
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
        distribuidor = kwargs.get('distribuidor_id')
        desarrollador = kwargs.get('desarrollador_id')
        modo_juego = kwargs.get('modo_juego_id')
        genero = kwargs.get('genero_id')
        plataforma = kwargs.get('plataforma_id')
        coleccion = kwargs.get('coleccion_id')
        carpeta = kwargs.get('carpeta_id')


        # Obtener todos los videojuegos
        # videojuegos = Videojuego.objects.all()

        # Obtener todos los videojuegos
        if not self.request.user.is_authenticated:
            videojuegos = Videojuego.objects.all()
        else:
            # Filtrar solo los videojuegos del usuario autenticado
            videojuegos = Videojuego.objects.filter(usuario=self.request.user)

        # Filtrar los objetos de Videojuego utilizando los filtros recibidos

        if nombre:
            # Filtrar por nombre escrito
            videojuegos = videojuegos.filter(nombre__icontains=nombre)

        if anio:
            # Filtrar por año escrito
            videojuegos = videojuegos.filter(anio__icontains=anio)

        if distribuidor:
            # Filtrar por distribuidor seleccionado
            videojuegos = videojuegos.filter(distribuidor__id=distribuidor)

        if desarrollador:
            # Filtrar por desarrollador seleccionado
            videojuegos = videojuegos.filter(desarrollador__id=desarrollador)

        if modo_juego:
            # Filtrar por modo de juego seleccionado
            videojuegos = videojuegos.filter(modo_juego__id=modo_juego)

        if genero:
            # Filtrar por genero seleccionado
            videojuegos = videojuegos.filter(genero__id=genero)

        if plataforma:
            # Filtrar por plataforma seleccionada
            videojuegos = videojuegos.filter(plataforma__id=plataforma)

        if coleccion:
            # Filtrar por colección seleccionada
            videojuegos = videojuegos.filter(coleccion_id=coleccion)

        if carpeta:
            # Filtrar por carpeta seleccionada
            videojuegos = videojuegos.filter(carpeta_id=carpeta)

        # Eliminar duplicados en Python
        def unique_videojuegos(videojuegos):
            seen = set()
            unique = []
            for videojuego in videojuegos:
                identifier = (videojuego.nombre, videojuego.anio)
                if identifier not in seen:
                    seen.add(identifier)
                    unique.append(videojuego)
            return unique

        # Obtener todos los videojuegos filtrados
        # context['videojuegos'] = videojuegos
        context['videojuegos'] = unique_videojuegos(videojuegos)

        return context


# -------------------------------- Recuperar videojuego al clickar en un videojuego de Panel
def videojuego_detail_view(request,pk):
    # videojuego = Videojuego.objects.get(pk=pk)
    videojuego = get_object_or_404(Videojuego, pk=pk)
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
        game_id = kwargs.get('id')
        context['videojuego'] = Videojuego.objects.get(id=game_id)
        return context





# Recopilación **************************************************************************************************
class RecopilacionCreateView(AreaRestringidaMixin, RecopilacionMixin, SuccessMessageMixin, CreateView):
    # model = Recopilacion
    # fields = ['nombre', 'descripcion', 'sinopsis', 'anio', 'img', 'distribuidor', 'desarrollador', 'modo_juego',
    #           'genero', 'plataforma', 'precio', 'edad_recomendada', 'tipo_contenido', 'tenemos', 'wish_list',
    #           'coleccion', 'formato', 'programa', 'carpeta', 'videojuegos']

    success_message = "Recopilación creada exitosamente"

    def form_valid(self, form):
        # Obtener el usuario actual
        user = self.request.user

        # Asignar el usuario actual al campo 'usuario' del formulario
        form.instance.usuario = user

        # Verificar si ya existe un videojuego con el mismo nombre y usuario
        if Videojuego.objects.filter(nombre=form.cleaned_data['nombre'],
                                     anio=form.cleaned_data['anio'],
                                     usuario=user).exists():
            form.add_error('nombre', 'Ya existe un videojuego con este nombre y año para tu cuenta.')
            return self.form_invalid(form)

        with transaction.atomic():
            # Guardar la instancia de la recopilación sin guardar las relaciones many-to-many
            self.object = form.save(commit=False)
            self.object.save()  # Guardar en la base de datos para obtener el ID

            # Ahora que la instancia tiene un ID, guardamos las relaciones many-to-many
            form.save_m2m()  # Esto guarda las relaciones many-to-many correctamente

            # Generar la sinopsis combinada si es necesario
            if not self.object.sinopsis:
                self.object.sinopsis = self.object.generate_combined_sinopsis()
                self.object.save()

        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Verificar si hay carpetas disponibles en la base de datos
        context['hay_carpetas'] = Carpeta.objects.exists()

        return context


class RecopilacionUpdateView(AreaRestringidaMixin, RecopilacionMixin, SuccessMessageMixin, UpdateView):
    model = Recopilacion

    success_message = "Recopilación editada exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class RecopilacionDeleteView(AreaRestringidaMixin, DeleteView):
    model = Recopilacion
    success_url = reverse_lazy('recopilacion')
    template_name = 'gamesapp/recopilacion_confirm_delete.html'


class RecopilacionListView(TemplateView):
    template_name = 'gamesapp/listado_recopilaciones.html'

    def get_context_data(self, **kwargs):
        context = super(RecopilacionListView, self).get_context_data(**kwargs)

        # Obtener los valores de los filtros enviados por el usuario
        nombre = self.request.GET.get('nombre')
        anio = self.request.GET.get('anio')

        # Sacar más de un registro al filtrar
        distribuidor = kwargs.get('distribuidor_id')
        desarrollador = kwargs.get('desarrollador_id')
        modo_juego = kwargs.get('modo_juego_id')
        genero = kwargs.get('genero_id')
        plataforma = kwargs.get('plataforma_id')
        coleccion = kwargs.get('coleccion_id')
        carpeta = kwargs.get('carpeta_id')

        # Obtener todas las recopilaciones
        if not self.request.user.is_authenticated:
            recopilaciones = Recopilacion.objects.all()
        else:
            # Filtrar solo las recopilaciones del usuario autenticado
            recopilaciones = Recopilacion.objects.filter(usuario=self.request.user)

        # Filtrar los objetos de Recopilacion utilizando los filtros recibidos

        if nombre:
            # Filtrar por nombre escrito
            recopilaciones = recopilaciones.filter(nombre__icontains=nombre)

        if anio:
            # Filtrar por año escrito
            recopilaciones = recopilaciones.filter(anio__icontains=anio)

        if distribuidor:
            # Filtar por distribuidor seleccionado
            recopilaciones = recopilaciones.filter(distribuidor__id=distribuidor)

        if desarrollador:
            # Filtrar por desarrollador seleccionado
            recopilaciones = recopilaciones.filter(desarrollador__id=desarrollador)

        if modo_juego:
            # Filtrar por modo de juego seleccionado
            recopilaciones = recopilaciones.filter(modo_juego__id=modo_juego)

        if genero:
            # Filtrar por género seleccionado
            recopilaciones = recopilaciones.filter(genero__id=genero)

        if plataforma:
            # Filtrar por plataforma seleccionada
            recopilaciones = recopilaciones.filter(plataforma__id=plataforma)

        if coleccion:
            # Filtrar por colección seleccionada
            recopilaciones = recopilaciones.filter(coleccion__id=coleccion)

        if carpeta:
            # Filtrar por carpeta seleccionada
            recopilaciones = recopilaciones.filter(carpeta__id=carpeta)

        # Eliminar duplicados en Python
        def unique_recopilaciones(recopilaciones):
            seen = set()
            unique = []
            for recopilacion in recopilaciones:
                identifier = (recopilacion.nombre, recopilacion.anio)
                if identifier not in seen:
                    seen.add(identifier)
                    unique.append(recopilacion)
                return unique

        # Obtener todas las recopilaciones filtradas
        context['recopilaciones'] = unique_recopilaciones(recopilaciones)

        return context


# --------------------- Recuperar la recopilación al clickar en una recopilación de Panel
def recopilacion_detail_view(request, pk):
    recopilacion = get_object_or_404(Recopilacion, pk=pk)
    context = {'recopilacion': recopilacion}
    return render(request, 'gamesapp/detalle_recopilacion.html', context)


# --------------------- Incluir código para que no explote la aplicación cuando se introduzca un id no válido.
# --------------------- Que devuelva la página 404 o el objeto
def recopilacionView(request, pk):
    recopilacion = get_object_or_404(Recopilacion, pk=pk)
    context = {'recopilacion': recopilacion}
    return render(request, 'gamesapp/listado_recopilaciones.html', context)


class RecopilacionDetailView(TemplateView):
    template_name = 'gamesapp/detalle_recopilacion.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        reco_id = kwargs.get('id')
        context['recopilacion'] = Recopilacion.objects.get(id=reco_id)
        return context

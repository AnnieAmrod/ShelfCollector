from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Genero, Carpeta
from .mixins import AreaRestringidaMixin, GeneroMixin, CarpetaMixin
from django.urls import reverse_lazy


# Create your views here.
class HomeView(TemplateView):
    template_name = 'common/home.html'


class PanelView(TemplateView):
    template_name = 'common/panel_inicio.html'


# CRUD
class GeneroCreateView(AreaRestringidaMixin, GeneroMixin, SuccessMessageMixin, CreateView):
    # model = Genero
    # fields = ['nombre', 'descripcion']

    success_message = "Género creado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class GeneroUpdateView(AreaRestringidaMixin, GeneroMixin, SuccessMessageMixin, UpdateView):
    model = Genero

    success_message = "Genero editado exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class GeneroDeleteView(AreaRestringidaMixin, DeleteView):
    model = Genero
    success_url = reverse_lazy('genero')
    template_name = 'common/genero_confirm_delete.html'


class GeneroListView(TemplateView):
    template_name = 'common/listado_generos.html'

    def get_context_data(self, **kwargs):
        context = super(GeneroListView, self).get_context_data(**kwargs)

        # Obtener los valores de los filtros enviados por el usuario
        nombre = self.request.GET.get('nombre')

        # Obtener todos los géneros
        if not self.request.user.is_authenticated:
            generos = Genero.objects.all()
        else:
            # Filtrar solo los géneros del usuario autenticado
            generos = Genero.objects.filter(usuario=self.request.user)

        # Filtrar los objetos de Genero utilizando los filtros recibidos
        if nombre:
            # Filtrar por nombre escrito
            generos = generos.filter(nombre__icontains=nombre)

        # Eliminar duplicados en Python
        def unique_generos(generos):
            seen = set()
            unique = []
            for genero in generos:
                identifier = (genero.nombre)
                if identifier not in seen:
                    seen.add(identifier)
                    unique.append(genero)
            return unique

        # Obtener todos los generos filtrados
        context['generos'] = unique_generos(generos)

        return context


# -------------------------------- Recuperar género al clickar en un género de Panel
def genero_detail_view(request,pk):
    genero = get_object_or_404(Genero, pk=pk)

    context = {'genero': genero}
    return render(request, 'common/detalle_genero.html', context)


# ------------------------------- Incluir código para que no explote la aplicación cuando se introduzca un id no válido.
    # -------------------------------- Que devuelva la página 404 o el objeto
def generoView(request, pk):
    genero = get_object_or_404(Genero, pk=pk)

    context = {'genero': genero}
    return render(request, 'common/listado_generos.html', context)


class GeneroDetailView(TemplateView):
    template_name = "common/detalle_genero.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        genre_id = kwargs.get('id')
        genero = Genero.objects.get(id=genre_id)

        context['genero'] = genero
        return context











class CarpetaCreateView(AreaRestringidaMixin, CarpetaMixin, SuccessMessageMixin, CreateView):
    # model = Carpeta
    # fields = ['nombre', 'descripcion']

    success_message = "Carpeta creada exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class CarpetaUpdateView(AreaRestringidaMixin, CarpetaMixin, SuccessMessageMixin, UpdateView):
    model = Carpeta

    success_message = "Carpeta editada exitosamente"

    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)


class CarpetaDeleteView(AreaRestringidaMixin, DeleteView):
    model = Carpeta
    success_url = reverse_lazy('carpeta')
    template_name = 'common/carpeta_confirm_delete.html'
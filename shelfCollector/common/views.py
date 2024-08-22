from django.shortcuts import render
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
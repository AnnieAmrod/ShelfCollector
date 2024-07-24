from django.contrib.messages.views import SuccessMessageMixin
from .models import Distibuidor
from django.urls import reverse_lazy
from .forms import (DistribuidorForm, DesarrolladorForm, ModoForm, PlataformaForm, EdadRecomendadaForm,
                    TipoContenidoForm, ColeccionForm, ProgramaForm)


class DistribuidorMixin(SuccessMessageMixin):
    # model = Distibuidor
    # fields = ['nombre', 'descripcion']
    form_class = DistribuidorForm
    template_name = 'gamesapp/distribuidor_form.html'

    # ---------------------------- Modificar la vista para que redireccione correctamente al crear un proyecto
        # Reverse lazy hace que, mediante el nombre, obtengamos la estructura de la url que queremos redireccionar
    def get_success_url(self):
        object = self.object
        return reverse_lazy('distribuidor_update', kwargs={'pk': object.id})


class DesarrolladorMixin(SuccessMessageMixin):
    form_class = DesarrolladorForm
    template_name = 'gamesapp/desarrollador_form.html'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('desarrollador_update', kwargs={'pk': object.id})


class ModoMixin(SuccessMessageMixin):
    form_class = ModoForm
    template_name = 'gamesapp/modo_form.html'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('modo_update', kwargs={'pk': object.id})


class PlataformaMixin(SuccessMessageMixin):
    form_class = PlataformaForm
    template_name = 'gamesapp/plataforma_form.html'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('plataforma_update', kwargs={'pk': object.id})


class EdadRecomendadaMixin(SuccessMessageMixin):
    form_class = EdadRecomendadaForm
    template_name = 'gamesapp/edad_recomendada_form.html'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('edad_recomendada_update', kwargs={'pk': object.id})


class TipoContenidoMixin(SuccessMessageMixin):
    form_class = TipoContenidoForm
    template_name = 'gamesapp/tipo_contenido_form.html'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('tipo_contenido_update', kwargs={'pk': object.id})


class ColeccionMixin(SuccessMessageMixin):
    form_class = ColeccionForm
    template_name = 'gamesapp/coleccion_form.html'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('coleccion_update', kwargs={'pk': object.id})


class ProgramaMixin(SuccessMessageMixin):
    form_class = ProgramaForm
    template_name = 'gamesapp/programa_form.html'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('programa_update', kwargs={'pk': object.id})

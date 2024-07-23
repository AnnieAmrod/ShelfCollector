from django.contrib.messages.views import SuccessMessageMixin
from .models import Distibuidor
from django.urls import reverse_lazy
from .forms import DistribuidorForm, DesarrolladorForm


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
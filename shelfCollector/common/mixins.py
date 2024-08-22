from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from .forms import GeneroForm, CarpetaForm
from django.urls import reverse_lazy



class AreaRestringidaMixin():
    @method_decorator(login_required)
    # *Sobreescribimos el método dispatch
    def dispatch(self, request, *args, **kwargs):
        # Si el user no está autenticado, lo redirigirá a la pantalla de login
        if not request.user.is_authenticated:
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)


class GeneroMixin(SuccessMessageMixin):
    form_class = GeneroForm
    template_name = 'common/genero_form.html'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('programa_update', kwargs={'pk': object.id})


class CarpetaMixin(SuccessMessageMixin):
    form_class = CarpetaForm
    template_name = 'common/carpeta_form.html'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('programa_update', kwargs={'pk': object.id})
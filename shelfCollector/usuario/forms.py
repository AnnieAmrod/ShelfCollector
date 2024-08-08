from django import forms
from .models import Usuario
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML, Field, Row


class UsuarioRegistradoForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'nombre']
    def __init__(self, *args, **kwargs):
        super(UsuarioRegistradoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Div(
                    Div(Field('nombre'), css_class="mb-4"),
                    Row(
                        Div(Field('email'), css_class="mb-6"),
                    ),
                    css_class="col-6"
                ),
            ),
        )

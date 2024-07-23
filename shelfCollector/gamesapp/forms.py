from django import forms
from .models import Distibuidor
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML, Field, Row


class DistribuidorForm(forms.ModelForm):
    class Meta:
        model = Distibuidor
        fields = ['nombre', 'descripcion']
    def __init__(self, *args, **kwargs):
        super(DistribuidorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Div(
                    Div(Field('nombre'), css_class="mb-4"),
                    css_class="col-6"
                ),
                Div(Field('descripcion'), css_class="col-12"),
            ),
        )

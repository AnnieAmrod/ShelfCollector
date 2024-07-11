from django import forms
from .models import Distibuidor


class DistribuidorForm(forms.ModelForm):
    class Meta:
        model = Distibuidor
        fields = ['nombre', 'descripcion']
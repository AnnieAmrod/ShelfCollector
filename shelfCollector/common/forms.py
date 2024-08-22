from django import forms
from .models import Genero, Carpeta


class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre', 'descripcion']


class CarpetaForm(forms.ModelForm):
    class Meta:
        model = Carpeta
        fields = ['nombre', 'descripcion']
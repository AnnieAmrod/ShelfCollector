from django import forms
from .models import Distibuidor, Desarrollador, Modo, Plataforma, EdadRecomendada, TipoContenido, Coleccion, Programa, Videojuego, Recopilacion
from common.models import Genero, Carpeta
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


class DesarrolladorForm(forms.ModelForm):
    class Meta:
        model = Desarrollador
        fields = ['nombre', 'descripcion']

    def __init__(self, *args, **kwargs):
        super(DesarrolladorForm, self).__init__(*args, **kwargs)
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


class ModoForm(forms.ModelForm):
    class Meta:
        model = Modo
        fields = ['modo_juego']


class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'


class PlataformaForm(forms.ModelForm):
    class Meta:
        model = Plataforma
        fields = ['nombre', 'retrocompatible']


class EdadRecomendadaForm(forms.ModelForm):
    class Meta:
        model = EdadRecomendada
        fields = '__all__'


class TipoContenidoForm(forms.ModelForm):
    class Meta:
        model = TipoContenido
        fields = ['nombre']


class ColeccionForm(forms.ModelForm):
    class Meta:
        model = Coleccion
        fields = ['nombre', 'descripcion', 'url']


class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = ['nombre', 'descripcion']


class CarpetaForm(forms.ModelForm):
    class Meta:
        model = Carpeta
        fields = '__all__'


class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = ['nombre', 'descripcion', 'sinopsis', 'anio', 'img', 'distribuidor', 'desarrollador', 'modo_juego',
                'genero', 'plataforma', 'precio', 'edad_recomendada', 'tipo_contenido', 'tenemos', 'wish_list',
                'coleccion', 'formato', 'programa', 'carpeta']


class RecopilacionForm(forms.ModelForm):
    class Meta:
        model = Recopilacion
        fields = ['nombre', 'descripcion', 'sinopsis', 'anio', 'img', 'distribuidor', 'desarrollador', 'modo_juego',
                'genero', 'plataforma', 'precio', 'edad_recomendada', 'tipo_contenido', 'tenemos', 'wish_list',
                'coleccion', 'formato', 'programa', 'carpeta', 'videojuegos']


class VideojuegoAdminForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(VideojuegoAdminForm, self).__init__(*args, **kwargs)
        self.fields['distribuidor'].queryset = Distibuidor.objects.all().order_by('nombre')
        self.fields['desarrollador'].queryset = Desarrollador.objects.all().order_by('nombre')
        self.fields['modo_juego'].queryset = Modo.objects.all().order_by('modo_juego')
        self.fields['genero'].queryset = Genero.objects.all().order_by('nombre')
        self.fields['plataforma'].queryset = Plataforma.objects.all().order_by('nombre')
        #self.fields['edad_recomendada'].queryset = EdadRecomendada.objects.all().order_by('numero')
        self.fields['coleccion'].queryset = Coleccion.objects.all().order_by('nombre')
        self.fields['programa'].queryset = Programa.objects.all().order_by('nombre')
        self.fields['carpeta'].queryset = Carpeta.objects.all().order_by('nombre')
from django import template
from ..models import Genero
register = template.Library()


@register.inclusion_tag('gamesapp/genero_dropdown_v.html')
def genero_dropdown_v():
    generos = Genero.objects.all().order_by('nombre')
    return {'generos': generos}

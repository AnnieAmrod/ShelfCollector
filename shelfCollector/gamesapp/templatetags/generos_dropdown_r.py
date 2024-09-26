from django import template
from ..models import Genero
register = template.Library()


@register.inclusion_tag('gamesapp/genero_dropdown_r.html')
def genero_dropdown_r():
    generos = Genero.objects.all().order_by('nombre')
    return {'generos': generos}

from django import template
from ..models import Genero
register = template.Library()


@register.inclusion_tag('gamesapp/genero_dropdown.html')
def genero_dropdown():
    generos = Genero.objects.all()
    return {'generos': generos}

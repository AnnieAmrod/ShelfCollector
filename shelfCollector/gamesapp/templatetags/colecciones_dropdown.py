from django import template
from ..models import Coleccion
register = template.Library()
@register.inclusion_tag('gamesapp/coleccion_dropdown.html')
def coleccion_dropdown():
    colecciones = Coleccion.objects.all()
    return {'colecciones': colecciones}

from django import template
from ..models import Coleccion
register = template.Library()


@register.inclusion_tag('gamesapp/coleccion_dropdown_v.html')
def coleccion_dropdown_v():
    colecciones = Coleccion.objects.all().order_by('nombre')
    return {'colecciones': colecciones}

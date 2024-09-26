from django import template
from ..models import Carpeta
register = template.Library()


@register.inclusion_tag('gamesapp/carpeta_dropdown_v.html')
def carpeta_dropdown_v():
    carpetas = Carpeta.objects.all().order_by('nombre')
    return {'carpetas': carpetas}

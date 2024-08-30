from django import template
from ..models import Carpeta
register = template.Library()


@register.inclusion_tag('gamesapp/carpeta_dropdown.html')
def carpeta_dropdown():
    carpetas = Carpeta.objects.all()
    return {'carpetas': carpetas}

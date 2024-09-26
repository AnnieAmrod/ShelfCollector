from django import template
from ..models import Desarrollador
register = template.Library()


@register.inclusion_tag('gamesapp/desarrollador_dropdown_v.html')
def desarrollador_dropdown_v():
    desarrolladores = Desarrollador.objects.all().order_by('nombre')
    return {'desarrolladores': desarrolladores}

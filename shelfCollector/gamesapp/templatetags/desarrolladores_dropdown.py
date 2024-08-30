from django import template
from ..models import Desarrollador
register = template.Library()


@register.inclusion_tag('gamesapp/desarrollador_dropdown.html')
def desarrollador_dropdown():
    desarrolladores = Desarrollador.objects.all()
    return {'desarrolladores': desarrolladores}

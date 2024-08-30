from django import template
from ..models import Modo
register = template.Library()


@register.inclusion_tag('gamesapp/modo_juego_dropdown.html')
def modo_juego_dropdown():
    modos_juego = Modo.objects.all()
    return {'modos_juego': modos_juego}

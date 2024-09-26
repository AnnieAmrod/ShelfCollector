from django import template
from ..models import Modo
register = template.Library()


@register.inclusion_tag('gamesapp/modo_juego_dropdown_v.html')
def modo_juego_dropdown_v():
    modos_juego = Modo.objects.all().order_by('modo_juego')
    return {'modos_juego': modos_juego}

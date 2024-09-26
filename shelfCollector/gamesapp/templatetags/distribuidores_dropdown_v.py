from django import template
from ..models import Distribuidor
register = template.Library()


@register.inclusion_tag('gamesapp/distribuidor_dropdown_v.html')
def distribuidor_dropdown_v():
    distribuidores = Distribuidor.objects.all().order_by('nombre')
    return {'distribuidores': distribuidores}

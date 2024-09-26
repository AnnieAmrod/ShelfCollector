from django import template
from ..models import Distribuidor
register = template.Library()


@register.inclusion_tag('gamesapp/distribuidor_dropdown_r.html')
def distribuidor_dropdown_r():
    distribuidores = Distribuidor.objects.all().order_by('nombre')
    return {'distribuidores': distribuidores}

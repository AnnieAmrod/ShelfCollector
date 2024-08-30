from django import template
from ..models import Distibuidor
register = template.Library()


@register.inclusion_tag('gamesapp/distribuidor_dropdown.html')
def distribuidor_dropdown():
    distribuidores = Distibuidor.objects.all()
    return {'distribuidores': distribuidores}

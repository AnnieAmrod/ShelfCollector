from django import template
from ..models import Plataforma
register = template.Library()


@register.inclusion_tag('gamesapp/plataforma_dropdown_v.html')
def plataforma_dropdown_v():
    plataformas = Plataforma.objects.all().order_by('nombre')
    return {'plataformas': plataformas}

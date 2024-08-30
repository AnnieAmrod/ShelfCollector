from django import template
from ..models import Plataforma
register = template.Library()


@register.inclusion_tag('gamesapp/plataforma_dropdown.html')
def plataforma_dropdown():
    plataformas = Plataforma.objects.all()
    return {'plataformas': plataformas}

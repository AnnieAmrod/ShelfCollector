from django.urls import path
from . import views

urlpatterns = [
    #path('funko_create/', views.DistribuidorCreateView.as_view(), name='funko_create'),
    path('coleccion_create/', views.ColeccionCreateView.as_view(), name='coleccion_create'),

    path('tamano_create/', views.TamanoCreateView.as_view(), name='tamano_create'),

    path('tipo_create/', views.TipoCreateView.as_view(), name='tipo_create'),

    path('funko_create/', views.FunkoCreateView.as_view(), name='funko_create'),

]

# if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
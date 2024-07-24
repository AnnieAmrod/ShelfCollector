from django.urls import path
from . import views

urlpatterns = [
    path('distribuidor_create/', views.DistribuidorCreateView.as_view(), name='distribuidor_create'),
    path('distribuidor_update/<int:pk>/', views.DistribuidorUpdateView.as_view(), name='distribuidor_update'),
    path('distribuidor_delete/<int:pk>/', views.DistribuidorDeleteView.as_view(), name='distribuidor_delete'),

    path('desarrollador_create/', views.DesarrolladorCreateView.as_view(), name='desarrollador_create'),
    path('desarrollador_update/<int:pk>/', views.DesarrolladorUpdateView.as_view(), name='desarrollador_update'),
    path('desarrollador_delete/<int:pk>/', views.DesarrolladorDeleteView.as_view(), name='desarrollador_delete'),

    path('modo_create/', views.ModoCreateView.as_view(), name='modo_create'),
    path('modo_update/<int:pk>/', views.ModoUpdateView.as_view(), name='modo_update'),
    path('modo_delete/<int:pk>/', views.ModoDeleteView.as_view(), name='modo_delete'),

    path('plataforma_create/', views.PlataformaCreateView.as_view(), name='plataforma_create'),
    path('plataforma_update/<int:pk>/', views.PlataformaUpdateView.as_view(), name='plataforma_update'),
    path('plataforma_delete/<int:pk>/', views.PlataformaDeleteView.as_view(), name='plataforma_delete'),

    path('edad_recomendada_create/', views.EdadRecomendadaCreateView.as_view(), name='edad_recomendada_create'),
    path('edad_recomendada_update/<int:pk>/', views.EdadRecomendadaUpdateView.as_view(), name='edad_recomendada_update'),
    path('edad_recomendada_delete/<int:pk>/', views.EdadRecomendadaDeleteView.as_view(), name='edad_recomendada_delete'),

    path('tipo_contenido_create/', views.TipoContenidoCreateView.as_view(), name='tipo_contenido_create'),
    path('tipo_contenido_update/<int:pk>/', views.TipoContenidoUpdateView.as_view(), name='tipo_contenido_update'),
    path('tipo_contenido_delete/<int:pk>/', views.TipoContenidoDeleteView.as_view(), name='tipo_contenido_delete'),

    path('coleccion_create/', views.ColeccionCreateView.as_view(), name='coleccion_create'),
    path('coleccion_update/<int:pk>/', views.ColeccionUpdateView.as_view(), name='coleccion_update'),
    path('coleccion_delete/<int:pk>/', views.ColeccionDeleteView.as_view(), name='coleccion_delete'),

    path('programa_create/', views.ProgramaCreateView.as_view(), name='programa_create'),
    path('programa_update/<int:pk>/', views.ProgramaUpdateView.as_view(), name='programa_update'),
    path('programa_delete/<int:pk>/', views.ProgramaDeleteView.as_view(), name='programa_delete'),

]

# if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
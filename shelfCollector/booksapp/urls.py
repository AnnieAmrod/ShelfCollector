from django.urls import path
from . import views

urlpatterns = [
    #path('funko_create/', views.DistribuidorCreateView.as_view(), name='funko_create'),
    path('autor_create/', views.AutorCreateView.as_view(), name='autor_create'),
    
    path('editorial_create/', views.EditorialCreateView.as_view(), name='editorial_create'),

    path('idioma_create/', views.IdiomaCreateView.as_view(), name='idioma_create'),

    path('libro_create/', views.LibroCreateView.as_view(), name='libro_create'),

]

# if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
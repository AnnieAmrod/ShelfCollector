from django.urls import path
from . import views
from usuario.views import LoginFormView, LogoutView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('panel/', views.PanelView.as_view(), name='panel'),
    # path('videojuegos/', views.VideojuegoListView.as_view(), name='videojuegos'),
    path('libro/', views.HomeView.as_view(), name='libro'),
    path('funko/', views.HomeView.as_view(), name='funko'),
    path('conocenos/', views.HomeView.as_view(), name='conocenos'),
    path('usuario_registrado_update/<int:pk>/', views.HomeView.as_view(), name='usuario_registrado_update'),
    path('login/', LoginFormView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),

    path('genero_create/', views.GeneroCreateView.as_view(), name='genero_create'),
    path('genero_update/<int:pk>/', views.GeneroUpdateView.as_view(), name='genero_update'),
    path('genero_delete/<int:pk>/', views.GeneroDeleteView.as_view(), name='genero_delete'),

    path('carpeta_create/', views.CarpetaCreateView.as_view(), name='carpeta_create'),
    path('carpeta_update/<int:pk>/', views.CarpetaUpdateView.as_view(), name='carpeta_update'),
    path('carpeta_delete/<int:pk>/', views.CarpetaDeleteView.as_view(), name='carpeta_delete'),

    path('generos/', views.GeneroListView.as_view(), name='generos'),
    path('genero/<int:id>/', views.GeneroDetailView.as_view(), name='genero_detail'),

]

# if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

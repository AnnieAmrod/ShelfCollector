from django.urls import path
from . import views
from usuario.views import LoginFormView, LogoutView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('panel/', views.PanelView.as_view(), name='panel'),
    path('videojuego/', views.HomeView.as_view(), name='videojuego'),
    path('libro/', views.HomeView.as_view(), name='libro'),
    path('funko/', views.HomeView.as_view(), name='funko'),
    path('conocenos/', views.HomeView.as_view(), name='conocenos'),
    path('usuario_registrado_update/<int:pk>/', views.HomeView.as_view(), name='usuario_registrado_update'),
    path('login/', LoginFormView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),

]

# if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

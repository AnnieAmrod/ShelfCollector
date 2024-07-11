from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('/home', views.HomeView.as_view(), name='home'),
    path('/panel', views.HomeView.as_view(), name='panel'),
    path('/videojuego', views.HomeView.as_view(), name='videojuego'),
    path('/libro', views.HomeView.as_view(), name='libro'),
    path('/funko', views.HomeView.as_view(), name='funko'),
    path('/conocenos', views.HomeView.as_view(), name='conocenos'),
    path('/usuario_registrado_update/<int:pk>', views.HomeView.as_view(), name='usuario_registrado_update'),
    path('/logout', views.HomeView.as_view(), name='logout'),
    path('/login', views.HomeView.as_view(), name='login'),

]

# if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views

urlpatterns = [
    path('distribuidor_create/', views.DistribuidorCreateView.as_view(), name='distribuidor_create'),
    path('distribuidor_update/<int:pk>/', views.DistribuidorUpdateView.as_view(), name='distribuidor_update'),
    path('distribuidor_delete/<int:pk>/', views.DistribuidorDeleteView.as_view(), name='distribuidor_delete'),
    path('desarrollador_create/', views.DesarrolladorCreateView.as_view(), name='desarrollador_create'),
    #path('desarrollador_update/<int:pk>/', views.DesarrolladorUpdateView.as_view(), name='desarrollador_update'),

]

# if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
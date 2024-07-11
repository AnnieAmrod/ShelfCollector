from django.urls import path
from . import views

urlpatterns = [
    path('distribuidor_create/', views.DistribuidorCreateView.as_view(), name='distribuidor_create'),
    path('distribuidor_update/<int:pk>/', views.DistribuidorUpdateView.as_view(), name='distribuidor_update'),
    path('distribuidor_delete/<int:pk>/', views.DistribuidorDeleteView.as_view(), name='distribuidor_delete')
]

# if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
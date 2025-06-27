from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Nuevo home
    path('subir-lote/', views.subir_lote, name='subir_lote'),
    path('resultado/<int:lote_id>/', views.resultado_lote, name='resultado_lote'),
]

# app/urls.py
from django.urls import path
from .views import (
    CreadorListView, CreadorDetailView, CreadorCreateView, CreadorUpdateView, CreadorDeleteView,
    VideojuegoListView, VideojuegoDetailView, VideojuegoCreateView, VideojuegoUpdateView, VideojuegoDeleteView, creadores_con_videojuegos, 
)
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/creadores-con-videojuegos/', creadores_con_videojuegos, name='creadores_con_videojuegos'),

    path('creadores/', CreadorListView.as_view(), name='creador_list'),
    path('creadores/<int:pk>/', CreadorDetailView.as_view(), name='creador_detail'),
    path('creadores/nuevo/', CreadorCreateView.as_view(), name='creador_create'),
    path('creadores/<int:pk>/editar/', CreadorUpdateView.as_view(), name='creador_update'),
    path('creadores/<int:pk>/eliminar/', CreadorDeleteView.as_view(), name='creador_delete'),

    path('videojuegos/', VideojuegoListView.as_view(), name='videojuego_list'),
    path('videojuegos/<int:pk>/', VideojuegoDetailView.as_view(), name='videojuego_detail'),
    path('videojuegos/nuevo/', VideojuegoCreateView.as_view(), name='videojuego_create'),
    path('videojuegos/<int:pk>/editar/', VideojuegoUpdateView.as_view(), name='videojuego_update'),
    path('videojuegos/<int:pk>/eliminar/', VideojuegoDeleteView.as_view(), name='videojuego_delete'),
]

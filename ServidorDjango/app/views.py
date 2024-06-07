# app/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Creador, Videojuego
from django.shortcuts import render

def index(request):
    return render(request, 'app/base.html')

@api_view(['GET'])
def creadores_con_videojuegos(request):
    creadores = Creador.objects.prefetch_related('videojuegos').all()
    data = []
    for creador in creadores:
        data.append({
            'nombre': creador.nombre,
            'videojuegos': [v.titulo for v in creador.videojuegos.all()]
        })
    return Response(data)


class CreadorListView(ListView):
    model = Creador

class CreadorDetailView(DetailView):
    model = Creador

class CreadorCreateView(CreateView):
    model = Creador
    fields = ['nombre', 'fecha_nacimiento']
    success_url = reverse_lazy('creador_list')

class CreadorUpdateView(UpdateView):
    model = Creador
    fields = ['nombre', 'fecha_nacimiento']
    success_url = reverse_lazy('creador_list')

class CreadorDeleteView(DeleteView):
    model = Creador
    success_url = reverse_lazy('creador_list')


class VideojuegoListView(ListView):
    model = Videojuego

class VideojuegoDetailView(DetailView):
    model = Videojuego

class VideojuegoCreateView(CreateView):
    model = Videojuego
    fields = ['titulo', 'fecha_lanzamiento', 'creador']
    success_url = reverse_lazy('videojuego_list')

class VideojuegoUpdateView(UpdateView):
    model = Videojuego
    fields = ['titulo', 'fecha_lanzamiento', 'creador']
    success_url = reverse_lazy('videojuego_list')

class VideojuegoDeleteView(DeleteView):
    model = Videojuego
    success_url = reverse_lazy('videojuego_list')

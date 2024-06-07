from django.db import models

# Create your models here.


class Creador(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Videojuego(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField()
    creador = models.ForeignKey(Creador, related_name='videojuegos', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

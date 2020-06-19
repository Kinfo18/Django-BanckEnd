from django.db import models


class Carrera(models.Model):
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=200)
    departamento = models.CharField(max_length=100)

def _str_(self):
    return self.codigo

class Meta:
    ordering = ['codigo']
    verbose_name = 'Carrera'
    verbose_name_plural = 'Carreras'
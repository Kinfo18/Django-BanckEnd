from django.db import models
from backend.carrera.models import carrera


class Estudiante(models.Model):
    carreraId = models.ForeignKey(
        Carrera, related_name="Estudiante", on_delete=models.CASCADE
    )
    
    documento = models.CharField(blank=True, max_length=100, verbose_name="documento")
    nombre = models.CharField(blank=True, max_length=100, verbose_name="nombre")
    apellido = models.CharField(blank=True, max_length=100, verbose_name="apellido")

def _str_(self):
    return self.documento

class Meta:
    ordering = ['documento']
    verbose_name = 'Estudiante'
    verbose_name_plural = 'Estudiante'
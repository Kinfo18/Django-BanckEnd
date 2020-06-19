from django.db import models
from backend.carrera.models import carrera


class Docente(models.Model):
    carreraId = models.ForeignKey(
        Carrera, related_name="Docente", on_delete=models.CASCADE
    )
    documento = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=200)

def _str_(self):
    return self.documento

class Meta:
    ordering = ['documento']
    verbose_name = 'Docente'
    verbose_name_plural = 'Docentes'

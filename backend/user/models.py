from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    usuario = None
    user_nombre = None
    user_apellido = None
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(_("email address"), unique=True)
    password = models.CharField(max_length=500)
    saltSecret = models.CharField(max_length=500, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nombre", "apellido", "password"]

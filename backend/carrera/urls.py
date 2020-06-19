from django.conf.urls import url
from rest_framework import routers
from .views import CarreraViewSet

router = routers.DefaultRouter()
router.register(r"carrera", CarreraViewSet)

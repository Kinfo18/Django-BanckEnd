from django.conf.urls import url
from rest_framework import routers
from .views import EstudianteRUDview, EstudianteAPIview, EstudianteRetrieveview

from .views import EstudianteViewSet

router = routers.DefaultRouter()
router.register(r'Estudiante', EEstudianteViewSet)

urlpatterns = [
    url(r"^$", EstudianteAPIview.as_view(), name="Estudiante-create"),
    url(r"^(?P<pk>\d+)/$", EstudianteRUDview.as_view(), name="Estudiante-rud"),
    url(
        r"^carrera/(?P<carreraId>\d+)/$",
        EmployeeRetrieveview.as_view(),
        name="Estudiante-retrieve",
    ),
]

from django.conf.urls import url
from rest_framework import routers
from .views import DocenteRUDview, DocenteAPIview, DocenteRetrieveview

urlpatterns = [
    url(r"^$", DocenteAPIview.as_view(), name="Docente-create"),
    url(r"^$", DocenteAPIview.as_view(), name="Docente-create"),
    url(r"^(?P<pk>\d+)/$", EmployeeRUDview.as_view(), name="Docente-rud"),
    url(
        r"^carrera/(?P<carreraId>\d+)/$",
        EmployeeRetrieveview.as_view(),
        name="Docente-retrieve",
    ),
]

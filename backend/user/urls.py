from django.conf.urls import url
from rest_framework import routers
from .views import UserRegisterView, UserLoginView


urlpatterns = [
    url(r"^register/$", UserRegisterView.as_view(), name="user-register"),
    url(r"^login/$", UserLoginView.as_view(), name="user-login"),
    url(r"^(?P<pk>\d+)/$", EstudianteRUDview.as_view(), name="Estudiante-rud"),
    url(
        r"^carrera/(?P<carreraId>\d+)/$",
        EstudianteRetrieveview.as_view(),
        name="Estudiante-retrieve",
    ),
]

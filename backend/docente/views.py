from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics, mixins

from rest_framework.permissions import IsAuthenticated, AllowAny
from backend.user.authentication import TokenAuthentication


from .models import Docente
from .serializers import DocenteSerializer

class DocenteAPIview(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    lookup_field = "pk"
    serializer_class = DocenteSerializer

    def get_queryset(self):
        qs = Docente.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(first_name__icontains=query) | Q(email__icontains=query)
            ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class DocenteRUDview(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    lookup_field = "pk"  
    serializer_class = DocenteSerializer

    def get_queryset(self):
        return Docente.objects.all()


class DocenteRetrieveview(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    lookup_field = "carreraId"
    serializer_class = DocenteSerializer

    def get_queryset(self, **kwargs):

        carreraId = self.request.parser_context["kwargs"]["carreraId"]
        return Docente.objects.filter(carreraId=carreraId)
from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics, mixins

from rest_framework.permissions import IsAuthenticated, AllowAny
from backend.user.authentication import TokenAuthentication

from rest_framework import viewsets
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response

from .models import Estudiante
from .serializers import EmployeeSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EmployeeSerializer

class EstudianteAPIview(generics.CreateAPIView):
    serializer_class = EstudianteSerializer

    def get_queryset(self):
    return Estudiante.objects.all()


class EstudianteAPIview(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    lookup_field = "pk"
    serializer_class = EstudianteSerializer

    def get_queryset(self):
        qs = Estudiante.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(first_name__icontains=query) | Q(email__icontains=query)
            ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class EstudianteRUDview(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    lookup_field = "pk" 
    serializer_class = EstudianteSerializer

    def get_queryset(self):
        return Estudiante.objects.all()


class EstudianteRetrieveview(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]
    lookup_field = "carreraId"
    serializer_class = EstudianteSerializer

    def get_queryset(self, **kwargs):
        queryset = Estudiante.objects.all()
        queryset = queryset.filter(carreraId=carreraId)
        carreraId = self.request.parser_context["kwargs"]["carreraId"]
        return Estudiante.objects.filter(carreraId=carreraId)


class EstudianteRetrieveview(APIView):
    def get_object(self, carreraId):
       try:
           return Estudiante.objects.get(carreraId=carreraId)
       except Estudiante.DoesNotExist:
           raise Http404

    def get(self, request, carreraId, format=None):
        Estudiante = self.get_object(carreraId)
        serializer = EstudianteSerializer(Estudiante)
        return Response(serializer.data)

from rest_framework import serializers
from .models import Estudiante


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ("documento", "carreraId", "nombre", "apellido")

    def create(self, validated_data):
        instance = Estudiante.objects.create(**validated_data)
        return instance

from rest_framework import serializers
from .models import Docente


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = ("documento", "carreraId", "nombre", "apellido", "email")

    def create(self, validated_data):
        instance = Docente.objects.create(**validated_data)
        return instance

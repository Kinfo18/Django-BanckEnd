from rest_framework import serializers
from .models import Carrera


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Carrera
        fields = ('codigo', 'nombre', 'departamento')

    def create(self, validated_data):
        instance = Carrera.objects.create(**validated_data)
        return instance

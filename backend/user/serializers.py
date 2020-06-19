from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
import bcrypt


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "nombre",
            "apellido",
            "email",
            "password",
            "saltSecret",
        )

    def create(self, validated_data):
        instance = User.objects.create(**validated_data)
        return instance

    def create(self, validated_data):
        salt = self.saltSecret()
        user = User.objects.create(
            nombre=validated_data["nombre"],
            apellido=validated_data["apellido"],
            email=validated_data["email"],
            password=bcrypt.hashpw(validated_data["password"].encode("utf8"), salt),
            saltSecret=salt
            password=make_password(validated_data["password"]),
        )
        user.save()
        return user

    def saltSecret(self):
        return bcrypt.gensalt()

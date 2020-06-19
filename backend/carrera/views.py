from django.shortcuts import render
from rest_framework import viewsets, views, status
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from .models import Carrera
from .serializers import CarreraSerializer
import json
import boto3
from botocore.client import Config
from backend.aws.conf import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_STORAGE_BUCKET_NAME,
    PUBLIC_URL,
)


class CarreraViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

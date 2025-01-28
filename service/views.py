from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.

class ServiceViewset(viewsets.ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer
class AvailableTimeViewset(viewsets.ModelViewSet):
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.availableTimeSerializer
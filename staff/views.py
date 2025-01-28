from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.
class StaffViewset(viewsets.ModelViewSet):
    queryset = models.Staff.objects.all()
    serializer_class = serializers.StaffSerializer


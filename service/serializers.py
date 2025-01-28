from rest_framework import serializers
from . import models

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'
class availableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AvailableTime
        fields = '__all__'
from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models
# Create your views here.
class BookingViewset(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer

    # custom query
    def get_queryset(self):
        queryset = super().get_queryset()
        member_id = self.request.query_params.get('member_id')
        if member_id:
            queryset = queryset.filter(member_id = member_id)
        return queryset
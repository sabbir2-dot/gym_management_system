from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AvailableTime(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="service/images/")
    fee = models.IntegerField()
    available_time = models.ManyToManyField(AvailableTime, blank=True)  # Fix the ManyToManyField warning
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.name
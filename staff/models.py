from django.db import models
from django.contrib.auth.models import User
from service.models import Service, AvailableTime
# Create your models here.

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='staff/images/')
    mobile_no = models.CharField(max_length=20)
    available_time = models.ManyToManyField(AvailableTime)
    service = models.ManyToManyField(Service)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
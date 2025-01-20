from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="service/images/")
    fee = models.IntegerField()

    def __str__(self):
        return self.name
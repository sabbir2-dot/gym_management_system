from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Contact Us"
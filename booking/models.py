from django.db import models
from staff.models import AvailableTime, Staff
from member.models import Member
# Create your models here.

BOOKING_TYPE = [
    ('Online','Online'),
    ('Offline','Offline'),
]

class Booking(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    booking_types = models.CharField(choices=BOOKING_TYPE, max_length=50)
    time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)

    def __str__(self):
        return f"Member {self.member.user.first_name}; Staff {self.staff.user.first_name}"

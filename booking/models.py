from django.db import models
from account.models import User

from package.models import HolidayPackage

# Create your models here.


class HolidayBooking(models.Model):
    id          = models.AutoField(primary_key=True)
    number      = models.CharField(max_length=255)
    no_adult    = models.IntegerField()
    no_children = models.IntegerField()
    package_id  = models.ForeignKey(HolidayPackage, on_delete=models.CASCADE)
    uid         = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_id  = models.CharField(max_length=255)
    start_date  = models.DateTimeField()
    end_date    = models.DateTimeField()
    
    def __str__(self):
        return self.number
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Meter(models.Model):
    number = models.IntegerField()
    brand = models.CharField(max_length =20)
    device = models.CharField(max_length=255)
    installed_at = models.DateField()
    expired_at = models.DateField()
    active = models.BooleanField()

class Data(models.Model):
    sender_device = models.CharField(max_length = 15)
    timestamp = models.DateTimeField()
    data = models.DecimalField(max_digits=15, decimal_places=3)
    received_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length = 25)
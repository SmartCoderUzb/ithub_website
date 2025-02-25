from django.db import models

# Create your models here.
class DeviceVisit(models.Model):
    device_id = models.CharField(max_length=255, unique=True)
    first_visit = models.DateTimeField(auto_now_add=True)
    last_visit = models.DateTimeField(auto_now=True)
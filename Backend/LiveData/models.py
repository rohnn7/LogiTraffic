from django.db import models
from Device.models import Device
# Create your models here.
class LiveData(models.Model):
    device = models.OneToOneField(Device, related_name='device', on_delete = models.CASCADE)
    speed = models.CharField(max_length=200, default='Speed', blank=False)
    logitude = models.CharField(max_length=200, default='Longitude', blank=False)
    latitude = models.CharField(max_length=200, default='Latitude', blank=False)
    live_image = models.ImageField(upload_to = 'live_image', blank = True)

    def __str__(self):
        return str(self.device.owner.username)
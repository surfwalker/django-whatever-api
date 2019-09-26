from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Surfer(models.Model):
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name

class Waves(models.Model):
    wavename = models.CharField(max_length=256)
    surfer = models.ForeignKey('Surfer', default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.wavename

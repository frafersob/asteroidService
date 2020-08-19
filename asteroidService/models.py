from django.db import models


class Asteroid(models.Model):
    dimensions = models.CharField(max_length=5, default='1x1')  # asumiendo resolucion maxima de 99x99
    matrix = models.CharField(max_length=100, default='1')


class AsteroidSighting(models.Model):
    date = models.DateField(default=None, blank=True, null=True)
    time = models.TimeField(default=None, blank=True, null=True)
    observatory_code = models.CharField(max_length=10, default='ob_0000000')
    device_code = models.CharField(max_length=8, default='de_00000')
    device_resolution = models.CharField(max_length=5, default='1x1')
    device_matrix = models.CharField(max_length=100, default='1')
    asteroid_code = models.IntegerField(default=None, blank=True, null=True)

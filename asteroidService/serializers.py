from rest_framework import serializers, viewsets
from .models import *


class AsteroidSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Asteroid
        fields = ('dimensions', 'matrix')


class AsteroidSightingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AsteroidSighting
        fields = ('date', 'time', 'observatory_code', 'device_code', 'device_resolution', 'device_matrix',
                  'asteroid_code')


class AsteroidViewSet(viewsets.ModelViewSet):
    queryset = Asteroid.objects.all()
    serializer_class = AsteroidSerializer


class AsteroidSightingViewSet(viewsets.ModelViewSet):
    queryset = AsteroidSighting.objects.all()
    serializer_class = AsteroidSightingSerializer

import csv

import numpy
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from asteroidProject.settings import SIGHTINGS_FILE
from asteroidService.models import Asteroid, AsteroidSighting
from asteroidService.serializers import AsteroidSightingSerializer


def readSightings(request):
    # Saltamos la primera linea
    with open(SIGHTINGS_FILE, newline='') as sightings:
        sightings_reader = csv.reader(sightings, delimiter='\t')
        next(sightings_reader)
        for sighting in sightings_reader:

            # Código de normalización
            dimensionsX = int(sighting[4].rpartition('x')[0])
            dimensionsY = int(sighting[4].rpartition('x')[2])

            # Creamos una matriz numpy con los datos de la matriz binaria y las dimensiones
            numpyMatrix = numpy.zeros((dimensionsY, dimensionsX))
            counter = 0
            for x in range(0, dimensionsY):
                for y in range(0, dimensionsX):
                    numpyMatrix[x][y] = int(sighting[5][counter])
                    counter += 1

            # Usamos masks de numpy para eliminar líneas y columnas con solo ceros
            numpyMatrix = numpyMatrix[:, ~(numpyMatrix == 0).all(0)]
            numpyMatrix = numpyMatrix[~(numpyMatrix == 0).all(1)]

            nDimensions = str(numpyMatrix.shape[1]) + "x" + str(numpyMatrix.shape[0])

            # Finalmente creamos la matriz normalizada
            nMatrix = ""
            for i in numpyMatrix:
                for j in i:
                    nMatrix += str(int(j))

            # Y la buscamos usando la matriz y dimensiones normalizadas como parámetro
            try:
                asteroid = Asteroid.objects.get(dimensions=nDimensions)

                # Si llegamos aquí, el asteroide existe, se crea sighting con su nueva clave
                newSighting = AsteroidSighting(date=sighting[0], time=sighting[1], observatory_code=sighting[2]
                                               , device_code=sighting[3], device_resolution=sighting[4]
                                               , device_matrix=sighting[5], asteroid_code=asteroid.id)
                newSighting.save()

            except Asteroid.DoesNotExist:
                # si no existe, se crea un nuevo asteroide y luego se coge la clave
                newAsteroid = Asteroid(dimensions=nDimensions, matrix=nMatrix)
                newAsteroid.save()

                newSighting = AsteroidSighting(date=sighting[0], time=sighting[1], observatory_code=sighting[2]
                                               , device_code=sighting[3], device_resolution=sighting[4]
                                               , device_matrix=sighting[5], asteroid_code=newAsteroid.id)
                newSighting.save()

    return JsonResponse({'message': 'File of Asteroid Sightings read and stored successfully'})



@api_view(['GET'])
def asteroidByMatrix(request, matrix, dimensions):

    # Código de normalización
    dimensionsX = int(dimensions.rpartition('x')[0])
    dimensionsY = int(dimensions.rpartition('x')[2])

    # Creamos una matriz numpy con los datos de la matriz binaria y las dimensiones
    numpyMatrix = numpy.zeros((dimensionsY, dimensionsX))
    counter = 0
    for x in range(0, dimensionsY):
        for y in range(0, dimensionsX):
            numpyMatrix[x][y] = int(matrix[counter])
            counter += 1

    # Usamos masks de numpy para eliminar líneas y columnas con solo ceros
    numpyMatrix = numpyMatrix[:, ~(numpyMatrix == 0).all(0)]
    numpyMatrix = numpyMatrix[~(numpyMatrix == 0).all(1)]

    nDimensions = str(numpyMatrix.shape[1]) + "x" + str(numpyMatrix.shape[0])

    # Finalmente creamos la matriz normalizada
    nMatrix = ""
    for i in numpyMatrix:
        for j in i:
            nMatrix += str(int(j))

    # Y la buscamos usando la matriz y dimensiones normalizadas como parámetro
    try:
        asteroid = Asteroid.objects.get(dimensions=nDimensions, matrix=nMatrix)

        sightings = AsteroidSighting.objects.filter(asteroid_code=asteroid.id)
        sightings_serializer = AsteroidSightingSerializer(sightings, many=True)
        return JsonResponse(sightings_serializer.data, status=200, safe=False)

    except Asteroid.DoesNotExist:
        return JsonResponse({'message': 'The asteroid does not exist'}, status=status.HTTP_404_NOT_FOUND)







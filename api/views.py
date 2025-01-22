from pprint import pprint
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from api.serializers import FilmSerializer, CreateFilmSerializer, UpdateFilmSerializer
from film.models import Film

from api.serializers import DetailFilmSerializer


@api_view(['GET', 'POST'])
def list_films(request, id=None):

    if request.method == 'POST':
        serializer = CreateFilmSerializer(data=request.data)
        if serializer.is_valid():
            film = serializer.save()
            read_serializer = DetailFilmSerializer(film, context={'request': request})
            return Response(read_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)


    films = Film.objects.all()
    serializer = FilmSerializer(films, many=True, context={'request': request})
    return Response(serializer.data)




@api_view(['GET', 'DELETE', 'PUT'])
def detail(request, id):
    film = get_object_or_404(Film, id=id)
    serializer = FilmSerializer(film, context={'request': request})
    pprint(serializer.data)

    if request.method == 'PUT':
        serializer = UpdateFilmSerializer(data=request.data, instance=film)
        if serializer.is_valid():
            film = serializer.save()
            read_serializer = DetailFilmSerializer(film, context={'request': request})
            return Response(read_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_200_OK)


    if request.method == 'DELETE':
        film = get_object_or_404(Film, id=id)
        film.delete()
        return Response({"detail": "фильм удалён"}, status=status.HTTP_204_NO_CONTENT)

    return Response(serializer.data)

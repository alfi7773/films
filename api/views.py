from pprint import pprint
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


from api.serializers import FilmSerializer
from film.models import Film

@api_view(['GET'])
def list_films(request):
    films = Film.objects.all()
    serializer = FilmSerializer(films, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, id):
    film = get_object_or_404(Film, id=id)
    serializer = FilmSerializer(film, context={'request': request})
    pprint(serializer.data)
    return Response(serializer.data)
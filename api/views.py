from pprint import pprint
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator
from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from api.serializers import (FilmSerializer, CreateFilmSerializer,
                             UpdateFilmSerializer, ImageForFilmSerializer,
                             FilmAttributeSerializer, FilmImageSerializer,
                             DetailFilmSerializer, UpdateProductAttributeSerializer
                             )
from film.models import Film, FilmImage, FilmAttribute

from .filters import FilmFilter
from rest_framework.generics import (ListAPIView, CreateAPIView, 
                                    RetrieveDestroyAPIView, RetrieveUpdateAPIView)

from rest_framework.views import APIView

from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer



class ListCreateFilmApiView(APIView):
    
    def get(self, request, *args, **kwargs):
        
        films = Film.objects.all()

        search = request.GET.get('search')
        if search:
            films = films.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search) |
                Q(category__name__icontains=search)
            ).distinct()

        filterset = FilmFilter(queryset=films, data=request.GET)
        films = filterset.qs

        ordering_fields = ['name', 'description', 'category', 'created_at']
        ordering: str = request.GET.get('ordering', '')
        tem_ordering = ordering.split('-')[1] if ordering.startswith('-') else ordering

        if tem_ordering in ordering_fields:
            films = films.order_by(ordering)

        # name = request.GET.get('name')
        # year = request.GET.get('year')
        # genre = request.GET.get('genre')
        #
        # if name:
        #     films = films.filter(name__icontains=name)
        # if year:
        #     films = films.filter(year=year)
        # if genre:
        #     films = films.filter(genre__name__icontains=genre)


        film_count = films.count()

        page = int(request.GET.get('page', 1))
        page_size = int(request.GET.get('page_size', 2))
        pagin = Paginator(films, page_size)
        films = pagin.get_page(page)

        serializer = FilmSerializer(films, many=True, context={'request': request})

        return Response({'page': page, 'page_size': page_size, 'count': film_count,'results': serializer.data})


    def post(self, request, *args, **kwargs):
        serializer = CreateFilmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        film = serializer.save()
        read_serializer = DetailFilmSerializer(film, context={'request': request})
        return Response(read_serializer.data, status=status.HTTP_201_CREATED)

    
class UpdateDetailDeleteApiView(APIView):
    
    def update(self, request, id, partial):
        film = get_object_or_404(Film, id=id)
        serializer = UpdateFilmSerializer(data=request.data, instance=film, partial=partial)
        serializer.is_valid(raise_exception=True)
        film = serializer.save()
        read_serializer = DetailFilmSerializer(film, context={'request': request})
        return Response(read_serializer.data)
        
    def get(self, request, id, *args, **kwargs):
        film = get_object_or_404(Film, id=id)
        serializer = FilmSerializer(film, context={'request': request})
        return Response(serializer.data)
        
    def put(self, request, id, *args, **kwargs):
        return self.update(request, id, partial=False)
    
    def patch(self, request, id, *args, **kwargs):
        return self.update(request, id, partial=True)
        
    def delete(self, request, id, *args, **kwargs):
        film = get_object_or_404(Film, id=id)
        film.delete()
        return Response({"detail": "фильм удалён"}, status=status.HTTP_204_NO_CONTENT)
    


class CreateAttrApiView(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = FilmAttributeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    

class UpdateDeleteAttrApiView(APIView):
    
    def update(self, request, id, partial):
        film_attr = get_object_or_404(FilmAttribute, id=id)
        serializer = UpdateProductAttributeSerializer(data=request.data, instance=film_attr, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get(self, request, id, *args, **kwargs):
        film_attr = get_object_or_404(FilmAttribute, id=id)
        serializer = FilmAttributeSerializer(film_attr)
        return Response(serializer.data)
    
    def put(self, request, id, *args, **kwargs):
        return self.update(request, id, partial=False)
        
    def patch(self, request, id, *args, **kwargs):
        return self.update(request, id, partial=True)
    
    def delete(self, request, id, *args, **kwargs):
        film_attr = get_object_or_404(FilmAttribute, id=id)
        serializer = FilmAttributeSerializer(film_attr)
        return Response(status=status.HTTP_204_NO_CONTENT)

    

class CreateImageApiView(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = FilmImageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
class DeleteImageApiView(APIView):
    
    def delete(self, request, id, *args, **kwargs):
        film_image = get_object_or_404(FilmImage, id=id)
        serializer = FilmImageSerializer(film_image)
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# Authorization
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"message": "Пользователь создан"}, status=status.HTTP_201_CREATED)





# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer


# class CustomTokenRefreshView(TokenRefreshView):
    # pass
    
    
# CRUD
# class ListFilm(ListAPIView):
#     serializer_class = FilmSerializer
#     queryset = Film.objects.all()
#     filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
#     filterset_class = FilmFilter
#     search_fields = ['name', 'description', 'year', 'category__name']
    
    
# class CreateFilm(CreateAPIView):
#     def get_serializer_class(self):
#         return CreateFilmSerializer
    
#     queryset = Film.objects.all()
    
    

# class DetailFilm(RetrieveDestroyAPIView):
#     serializer_class = DetailFilmSerializer
#     queryset = Film.objects.all()
#     lookup_field = 'id'
    
    
# class UpdateFilm(RetrieveUpdateAPIView):
#     serializer_class = UpdateFilmSerializer
#     queryset = Film.objects.all()
#     lookup_field = 'id'



# first form serializers
# class FilmPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 100


# @api_view(['GET', 'POST'])
# def list_films(request, id=None):
#     if request.method == 'POST':
#         serializer = CreateFilmSerializer(data=request.data)
#         if serializer.is_valid():
#             film = serializer.save()
#             read_serializer = DetailFilmSerializer(film, context={'request': request})
#             return Response(read_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     films = Film.objects.all()

#     search = request.GET.get('search')
#     if search:
#         films = films.filter(
#             Q(name__icontains=search) |
#             Q(description__icontains=search) |
#             Q(category__name__icontains=search)
#         ).distinct()

#     filterset = FilmFilter(queryset=films, data=request.GET)
#     films = filterset.qs

#     ordering_fields = ['name', 'description', 'category', 'created_at']
#     ordering: str = request.GET.get('ordering', '')
#     tem_ordering = ordering.split('-')[1] if ordering.startswith('-') else ordering

#     if tem_ordering in ordering_fields:
#         films = films.order_by(ordering)

#     # name = request.GET.get('name')
#     # year = request.GET.get('year')
#     # genre = request.GET.get('genre')
#     #
#     # if name:
#     #     films = films.filter(name__icontains=name)
#     # if year:
#     #     films = films.filter(year=year)
#     # if genre:
#     #     films = films.filter(genre__name__icontains=genre)


#     film_count = films.count()

#     page = int(request.GET.get('page', 1))
#     page_size = int(request.GET.get('page_size', 2))
#     pagin = Paginator(films, page_size)
#     films = pagin.get_page(page)

#     serializer = FilmSerializer(films, many=True, context={'request': request})

#     return Response({'page': page, 'page_size': page_size, 'count': film_count,'results': serializer.data})



# @api_view(['GET', 'DELETE', 'PUT', 'PATCH'])
# def detail(request, id):
#     film = get_object_or_404(Film, id=id)
#     serializer = FilmSerializer(film, context={'request': request})
#     pprint(serializer.data)

#     if request.method in ['PATCH', 'PUT']:
#         partial = request.method == 'PATCH'
#         serializer = UpdateFilmSerializer(data=request.data, instance=film, partial=partial)
#         if serializer.is_valid():
#             film = serializer.save()
#             read_serializer = DetailFilmSerializer(film, context={'request': request})
#             return Response(read_serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_200_OK)


#     if request.method == 'DELETE':
#         film = get_object_or_404(Film, id=id)
#         film.delete()
#         return Response({"detail": "фильм удалён"}, status=status.HTTP_204_NO_CONTENT)

#     return Response(serializer.data)

# @api_view(['POST'])
# def create_film_image(request):
#     serializer = FilmImageSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def create_film_attr(request):
#     serializer = FilmAttributeSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status.HTTP_201_CREATED)



# @api_view(['DELETE'])
# def delete_film_image(request, id):
#     image = FilmImage.objects.get(id=id)
#     image.delete()
#     return Response(request, {'message': 'удалено '}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['PUT', 'PATCH', 'DELETE'])
# def update_delete_film_attr(request, id):
#     film_attr = get_object_or_404(FilmAttribute, id=id)
#     if request.method in ['PATCH', 'PUT']:
#         partial = request.method == 'PATCH'
#         serializer = FilmAttributeSerializer(data=request.data, instance=film_attr, partial=partial)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_200_OK)

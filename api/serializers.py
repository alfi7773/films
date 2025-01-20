from rest_framework import serializers
from django.contrib.auth.models import User

from film.models import Film, Genre, Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        product = User
        fields = ('name',)

class FilmSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    category = CategorySerializer()
    image = serializers.ImageField()
    # user = UserSerializer()


    class Meta:
        model = Film
        exclude = ('description',)



class DetailFilmSerializer(serializers.ModelSerializer):

    genre = GenreSerializer()
    category = CategorySerializer()
    image = serializers.ImageField()
    user = UserSerializer()

    class Meta:
        model = Film
        fields = '__all__'

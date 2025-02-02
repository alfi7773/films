from rest_framework import serializers
from django.contrib.auth.models import User
from utils.main import base64_to_image_file
import uuid
from rest_framework.pagination import PageNumberPagination


from film.models import Film, Genre, Category

from film.models import FilmAttribute, FilmImage
from rest_framework import serializers
from django.contrib.auth.models import User



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user




class AttributeForFilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = FilmAttribute
        exclude = ('film',)


class ImageForFilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = FilmImage
        exclude = ('film',)

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
        model = User
        fields = ('username',)

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
    # user = serializers.ListSerializer(child=serializers.CharField(source='user.name'))

    class Meta:
        model = Film
        fields = '__all__'


class CreateFilmSerializer(serializers.ModelSerializer):

    attributes = AttributeForFilmSerializer(many=True, required=False)
    image = serializers.ListSerializer(child=serializers.CharField(), required=False)

    class Meta:
        model = Film
        fields = '__all__'


    def create(self, validated_data):
        attributes = validated_data.pop('attributes', [])
        images = validated_data.pop('image', [])

        file_images = []

        for image in images:
            try:
                file = base64_to_image_file(image, uuid.uuid4())
                file_images.append(file)
            except Exception as e:
                print(e)
                raise serializers.ValidationError(
                    {'images': ['Загрузите корректное изображение']}
                )

        film = Film.objects.create(**validated_data)


        for attribute in attributes:
            FilmAttribute.objects.create(
                **attribute,
                film=film
            )

        for file in file_images:
            film_image = FilmImage.objects.create(film=film)
            film_image.image.save(file.name, file)
            film_image.save()

        return film



class UpdateFilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = '__all__'


    def update(self, instance, validated_data):
        attributes = validated_data.pop('attributes', [])
        images = validated_data.pop('image', [])

        file_images = []

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if attributes:
            FilmAttribute.objects.filter(film=instance).delete()

        for attribute in attributes:
            FilmAttribute.objects.create(
                **attribute,
                film=film
            )

        if images:
            FilmImage.objects.filter(film=instance).delete()


        for image in images:
            try:
                file = base64_to_image_file(image, uuid.uuid4())
                file_images.append(file)
            except Exception as e:
                print(e)
                raise serializers.ValidationError(
                    {'images': ['Загрузите корректное изображение']}
                )

        # film = Film.objects.update(**validated_data, film=instance)


        for file in file_images:
            film_image = FilmImage.objects.create(film=film)
            film_image.image.save(file.name, file)
            film_image.save()


        return instance

class FilmImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FilmImage
        fields = '__all__'

class FilmAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FilmAttribute
        fields = '__all__'

class UpdateProductAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FilmAttribute
        fields = ('name', 'value')
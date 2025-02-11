from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.utils.timezone import now
from account.services import User




class TimeStampAbstractModel(models.Model):
    created_at = models.DateTimeField('дата добавление', auto_now_add=True)
    updated_at = models.DateTimeField('дата изменения', auto_now=True)

    class Meta:
        abstract = True


class Genre(TimeStampAbstractModel):

    class Meta:
        verbose_name_plural = "жанры"
        verbose_name = 'жанр'

    name = models.CharField(verbose_name='имя жанра', max_length=100)

    def __str__(self):
        return self.name


class Category(TimeStampAbstractModel):

    class Meta:
        verbose_name_plural = "категории"
        verbose_name = 'категория'

    name = models.CharField(verbose_name='категория', max_length=100)

    def __str__(self):
        return self.name


class NewsFilm(TimeStampAbstractModel):

    class Meta:
        verbose_name_plural = 'новости'
        verbose_name = 'новость'

    name = models.CharField(verbose_name='имя', max_length=100)
    description = models.CharField(verbose_name='описание', max_length=300)
    image = models.ImageField(verbose_name='изображение новостя', upload_to='media_films')
    category = models.ForeignKey('film.Category', on_delete=models.PROTECT, related_name='news')

    def __str__(self):
        return self.name


class Film(TimeStampAbstractModel):

    class Meta:
        verbose_name_plural = "фильмы"
        verbose_name = 'фильм'

    name = models.CharField(verbose_name='название фильма',max_length=100)
    description = models.TextField(verbose_name='описание', max_length=800)
    year = models.IntegerField(verbose_name='год производства')
    # image = models.ImageField(verbose_name='изображение фильма', upload_to='media_films/')
    category = models.ForeignKey('film.Category', on_delete=models.PROTECT, related_name='film')
    genre = models.ManyToManyField('film.Genre')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user', blank=True, null=True)


    @property
    def image(self):
        if self.images.first():
            return self.images.first().image
        return None


    def __str__(self):
        return self.name


class FilmImage(TimeStampAbstractModel):
    class Meta:
        verbose_name = 'изображение товара'
        verbose_name_plural = 'изображении товаров'
        ordering = ('-created_at',)

    film = models.ForeignKey('film.Film', models.CASCADE, related_name='images', verbose_name='фильм')
    image = ResizedImageField('изображение', upload_to='film_images/', quality=90, force_format='WEBP')

    def __str__(self):
        return f'{self.film.name}'


class FilmAttribute(TimeStampAbstractModel):
    class Meta:
        verbose_name = 'атрибут товара'
        verbose_name_plural = 'атрибуты товаров'
        ordering = ('-created_at',)

    name = models.CharField('название', max_length=50)
    value = models.CharField('значение', max_length=50)
    film = models.ForeignKey('film.Film', models.CASCADE, related_name='attributes', verbose_name='фильм')

    def __str__(self):
        return f'{self.name} - {self.value}'


# Create your models here.

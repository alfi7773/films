from django.db import models


class Genre(models.Model):

    class Meta:
        verbose_name_plural = "жанры"
        verbose_name = 'жанр'

    name = models.CharField(verbose_name='имя жанра', max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):

    class Meta:
        verbose_name_plural = "категории"
        verbose_name = 'категория'

    name = models.CharField(verbose_name='категория', max_length=100)

    def __str__(self):
        return self.name


class NewsFilm(models.Model):

    class Meta:
        verbose_name_plural = 'новости'
        verbose_name = 'новость'

    name = models.CharField(verbose_name='имя', max_length=100)
    description = models.CharField(verbose_name='описание', max_length=300)
    image = models.ImageField(verbose_name='изображение новостя', upload_to='media_films')
    category = models.ForeignKey('film.Category', on_delete=models.PROTECT, related_name='news')

    def __str__(self):
        return self.name


class Film(models.Model):

    class Meta:
        verbose_name_plural = "фильмы"
        verbose_name = 'фильм'

    name = models.CharField(verbose_name='название фильма',max_length=100)
    description = models.TextField(verbose_name='описание', max_length=800)
    year = models.IntegerField(verbose_name='год производства')
    image = models.ImageField(verbose_name='изображение фильма', upload_to='media_films/')
    category = models.ForeignKey('film.Category', on_delete=models.PROTECT, related_name='film')
    genre = models.ForeignKey('film.Genre', on_delete=models.PROTECT, related_name='film')



    def __str__(self):
        return self.name


# Create your models here.

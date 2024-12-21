from django.contrib import admin

from .models import Film, Category, Genre, NewsFilm

admin.site.register(Film)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(NewsFilm)


# Register your models here.


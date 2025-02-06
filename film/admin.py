from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Film, Category, Genre, NewsFilm, FilmImage, FilmAttribute

# admin.site.register(Film)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(NewsFilm)


class FilmImageStackedInline(admin.TabularInline):

    model = FilmImage
    extra = 1


class FilmAttributeStackedInline(admin.TabularInline):

    model = FilmAttribute
    extra = 1


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'category', 'get_image')
    list_display_links = ('id', 'name',)
    list_filter = ('category', 'genre', 'user', 'year',)
    search_fields = ('name', 'description', 'year',)
    readonly_fields = ('created_at', 'updated_at', 'get_big_image',)
    inlines = [FilmAttributeStackedInline, FilmImageStackedInline]

    @admin.display(description='Изображение')
    def get_image(self, item):
        if item.image:
            return mark_safe(f'<img src="{item.image.url}" width="150px">')
        return '-'

    @admin.display(description='Изображение')
    def get_big_image(self, item):
        if item.image:
            return mark_safe(f'<img src="{item.image.url}" width="100%">')
        return '-'


# Register your models here.


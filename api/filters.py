import django_filters
from film.models import Film

class FilmFilter(django_filters.FilterSet):
    date = django_filters.NumberFilter(field_name='created_at')

    class Meta:
        model = Film
        fields = ['category', 'date']
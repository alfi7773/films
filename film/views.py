from django.shortcuts import render, get_object_or_404
from .models import *


def main(request):
    films = Film.objects.all()
    return render(request, 'index.html', {
    'films':films,
    })

def detail(request, id):
    film = get_object_or_404(Film, id=id)
    return render(request, 'in.html', {
        'film': film,
    })
# Create your views here.

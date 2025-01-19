from django.shortcuts import render
from .models import *


def main(request):
    films = Film.objects.all()
    return render(request, 'base.html', {
    'films':films,
    })
# Create your views here.

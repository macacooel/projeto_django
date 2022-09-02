from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'leonardo',
    })


def contato(request):
    return render(request, 'tmp.html')


def sobre(request):
    return HttpResponse('Sobre')

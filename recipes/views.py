
from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html', context={
        'name': 'leonardo',
    })


def recipe(request, id):
    return render(request, 'pages/recipe-view.html', context={
        'name': 'leonardo',
    })

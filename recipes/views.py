
from django.shortcuts import render
from ultis.recipes.factory import make_recipe


def home(request):
    return render(request, 'pages/home.html', context={
        'recipes': [make_recipe() for _ in range(3)],
    })


def recipe(request, id):
    return render(request, 'pages/recipe-view.html', context={
        'recipe': make_recipe(),

    })

from django.shortcuts import render
from recipes.models import Recipe


def home(request,):
    recipes = Recipe.objects.all()
    return render(
        request,
        'recipes/pages/home.html',
        {
            'recipe': recipes,
            'page_title': 'Home - '
        }
    )

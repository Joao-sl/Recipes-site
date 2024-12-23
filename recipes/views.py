from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from recipes.models import Recipe, Category
from django.db.models import Q


def home(request,):
    recipes = Recipe.objects.all().filter(show_recipe=True).order_by('-id')[:8]
    categories = Category.objects.all().order_by('id')

    return render(
        request,
        'recipes/pages/home.html',
        {
            'recipes': recipes,
            'categories': categories,
            'page_title': 'Home'
        }
    )


def recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug, show_recipe=True)
    categories = Category.objects.all().order_by('id')
    ingredients_list = recipe.ingredients.split('//')
    directions_list = recipe.directions.split('//')

    return render(
        request,
        'recipes/pages/recipe.html',
        {
            'recipe': recipe,
            'page_title': recipe.recipe_title,
            'categories': categories,
            'ingredients_list': ingredients_list,
            'directions_list': directions_list,
        }
    )


def categories(request):
    categories = Category.objects.all().order_by('id')

    return render(
        request,
        'recipes/pages/categories.html',
        {
            'page_title': 'Categorias',
            'categories': categories,
        }
    )


def search(request):
    search_value = request.GET.get('q', '').strip()
    categories = Category.objects.all().order_by('id')

    # O "Q" me permite fazer uma pesquisa, e o "|" é um ou
    recipes = Recipe.objects.filter(
        Q(recipe_title__icontains=search_value) |
        Q(difficulty__icontains=search_value) |
        Q(category__name__icontains=search_value)
    ).filter(show_recipe=True)

    if not search_value:
        return redirect('recipes:home')

    paginator = Paginator(recipes, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'recipes/pages/home.html',
        {
            'recipes': page_obj,
            'page_title': search_value,
            'search_value': search_value,
            'categories': categories,
        }
    )


def category_search(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    categories = Category.objects.all().order_by('id')
    category_recipes = Recipe.objects.filter(
        category=category,
        show_recipe=True
    )

    # Mudar a quantidade por página depois.
    paginator = Paginator(category_recipes, 12)
    page_number = request.GET.get('page')
    recipes = paginator.get_page(page_number)

    return render(
        request,
        'recipes/pages/home.html',
        {
            'recipes': recipes,
            'page_title': category,
            'categories': categories,
        }
    )

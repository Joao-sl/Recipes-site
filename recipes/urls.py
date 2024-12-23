from django.urls import path
from recipes.views import home, recipe, categories, search, category_search

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('recipe/<str:slug>/', recipe, name='recipe'),
    path('categories/', categories, name='categories'),
    path('search/', search, name='search'),
    path(
        'categories/<str:category_name>',
        category_search,
        name='category_search'
    ),
]

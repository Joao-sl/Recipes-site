from django.urls import path
from recipes.views import home

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
]

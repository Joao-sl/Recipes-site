from django.db import models
from utils.time_preparation_validation import time_validator


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


# Deixa o código mais robusto e facilita a manutenção e da possibilidade de
# if Recipe.difficulty == Difficulty.MEDIO:
class Difficulty(models.TextChoices):
    FACIL = 'Facil', 'Fácil'
    MEDIO = 'Medio', 'Médio'
    DIFICIL = 'Dificil', 'Difícil'


class Recipe(models.Model):
    class Meta:
        verbose_name = 'Register Recipe'
        verbose_name_plural = 'Register Recipes'

    recipe_title = models.CharField(max_length=70,)

    ingredients = models.TextField(
        max_length=1000,
        help_text='Separe os ingredientes por virgulas. Exemplo Cebola, Tomate, Alho',
    )

    directions = models.TextField(
        max_length=2000,
        help_text='Separe os passos por virgulas. Exemplo Passo 1, Passo 2, Passo 3'
    )

    preparation_time = models.CharField(
        max_length=9,
        help_text='Exemplos: 30min ou 1h 25min, etc',
        validators=[time_validator],
        null=True
    )

    difficulty = models.CharField(max_length=7, choices=Difficulty.choices,)

    tips = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        help_text='Campo não obrigatório',
    )

    recipe_image = models.ImageField(
        upload_to='assets/recipe_images/%Y/%m',
        blank=True,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    show_recipe = models.BooleanField(default=True)

    def __str__(self):
        return self.recipe_title

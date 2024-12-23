from django.db import models
from utils.time_preparation_validation import time_validator
from django.utils.text import slugify
from utils.img_resizer import resize_image, if_image_changed, if_image_changed_category


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=36, unique=True, null=True)

    category_image = models.ImageField(
        upload_to='assets/category_images/%Y/%m',
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        if self.category_image and if_image_changed_category(self):
            resized_image = resize_image(
                self.category_image,
                height=168,
                width=168,
            )
            self.category_image = resized_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# Facilita a manutenção
class Difficulty(models.TextChoices):
    FACIL = 'Facil', 'Fácil'
    MEDIO = 'Medio', 'Médio'
    DIFICIL = 'Dificil', 'Difícil'


class Recipe(models.Model):
    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    recipe_title = models.CharField(max_length=70, unique=True,)
    slug = models.SlugField(unique=True, blank=True, null=True,)

    ingredients = models.TextField(
        max_length=1000,
        help_text='Separe os ingredientes por duas barras. Exemplo Cebola // Tomate // Alho',
    )

    directions = models.TextField(
        max_length=2000,
        help_text='Separe os passos por duas barras. Exemplo Passo 1 // Passo 2 // Passo 3'
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
        max_length=255,
        help_text='Envie imagens como o nome de no MÁXIMO 200 caracteres',
        null=False,
        blank=False,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
    )

    servings = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        help_text='Campo não obrigatório'
    )

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    show_recipe = models.BooleanField(default=True)

    # A slug vai ser o titulo da receita, se for alterado a slug também será
    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.recipe_title):
            self.slug = slugify(self.recipe_title)
            # Garantir que o slug seja único
            original_slug = self.slug
            counter = 1
            while Recipe.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1

        if self.recipe_image and if_image_changed(self):
            resized_image = resize_image(
                self.recipe_image,
                height=400,
                width=840,
                quality=70,
                optimize=True,
            )
            self.recipe_image = resized_image

        super().save(*args, **kwargs)

    def __str__(self):
        return self.recipe_title

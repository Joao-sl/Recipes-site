from django.db import models
from utils.time_preparation_validation import time_validator
from django.utils.text import slugify
from utils.img_resizer import resize_image, if_image_changed, if_image_changed_category


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(
        max_length=36,
        unique=True,
        null=True,
        verbose_name='Nome',
    )

    category_image = models.ImageField(
        upload_to='assets/category_images/%Y/%m',
        blank=True,
        null=True,
        verbose_name='Imagem da categoria',
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

    recipe_title = models.CharField(
        max_length=70,
        unique=True,
        verbose_name='Título da receita',
    )

    slug = models.SlugField(unique=True, blank=True, null=True,)

    ingredients = models.TextField(
        max_length=1000,
        help_text='Separe os ingredientes por duas barras. Exemplo Cebola // Tomate // Alho',
        verbose_name='Ingredientes',
    )

    directions = models.TextField(
        max_length=2000,
        help_text='Separe os passos por duas barras. Exemplo Passo 1 // Passo 2 // Passo 3',
        verbose_name='Modo de Preparo',
    )

    preparation_time = models.CharField(
        max_length=9,
        help_text='Exemplos: 30min ou 1h 25min, etc',
        validators=[time_validator],
        null=True,
        verbose_name='Tempo de Preparo',
    )

    difficulty = models.CharField(
        max_length=7,
        choices=Difficulty.choices,
        verbose_name='Dificuldade',
    )

    tips = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        help_text='Campo não obrigatório',
        verbose_name='Dicas',
    )

    recipe_image = models.ImageField(
        upload_to='assets/recipe_images/%Y/%m',
        max_length=255,
        help_text='Envie imagens como o nome de no MÁXIMO 200 caracteres',
        null=False,
        blank=False,
        verbose_name='Imagem da Receita',
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Categoria',
    )

    servings = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        help_text='Campo não obrigatório',
        verbose_name='Porções',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        verbose_name='Criado em:',
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        verbose_name='Atualizado em:',
    )

    show_recipe = models.BooleanField(
        default=True,
        verbose_name='Mostrar receita',
    )

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

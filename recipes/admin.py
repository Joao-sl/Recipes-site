from django.contrib import admin
from recipes.models import Recipe, Category


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = 'id', 'recipe_title', 'category', 'difficulty',
    list_display_links = 'id', 'recipe_title',
    search_fields = 'id', 'recipe_title',
    readonly_fields = 'created_at', 'updated_at', 'slug'

    # Apenas para sumir com o pop-up de edição
    autocomplete_fields = 'category',
    raw_id_fields = 'category',


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'
    list_display_links = 'id', 'name'
    search_fields = 'id', 'name',

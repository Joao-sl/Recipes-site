# Generated by Django 5.1.3 on 2024-12-23 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_alter_recipe_options_recipe_servings_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='servings',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Campo não obrigatório', null=True),
        ),
    ]

# Generated by Django 5.1.3 on 2024-12-04 18:16

import utils.time_preparation_validation
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='tips',
            field=models.TextField(blank=True, help_text='Campo não obrigatório', max_length=278, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(max_length=278),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation_time',
            field=models.CharField(help_text='Exemplos: 30min ou 1h 25min, etc', max_length=9, validators=[utils.time_preparation_validation.time_validator]),
        ),
    ]

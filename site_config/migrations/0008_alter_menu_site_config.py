# Generated by Django 5.1.3 on 2024-12-02 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_config', '0007_alter_menu_site_config'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='site_config',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='site_config.siteconfig'),
        ),
    ]

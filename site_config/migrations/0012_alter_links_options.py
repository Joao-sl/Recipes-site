# Generated by Django 5.1.3 on 2024-12-02 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_config', '0011_rename_menu_links'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='links',
            options={'verbose_name': 'Link', 'verbose_name_plural': 'Links'},
        ),
    ]

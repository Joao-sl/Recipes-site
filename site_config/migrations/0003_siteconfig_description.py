# Generated by Django 5.1.3 on 2024-12-02 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_config', '0002_siteconfig_alter_menu_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='description',
            field=models.CharField(default='', max_length=278),
        ),
    ]

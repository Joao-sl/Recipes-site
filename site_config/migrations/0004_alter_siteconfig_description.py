# Generated by Django 5.1.3 on 2024-12-02 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_config', '0003_siteconfig_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfig',
            name='description',
            field=models.CharField(max_length=278),
        ),
    ]

# Generated by Django 5.1.3 on 2024-12-02 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=78)),
                ('url', models.CharField(max_length=2048)),
                ('open_new_tab', models.BooleanField(default=False)),
            ],
        ),
    ]
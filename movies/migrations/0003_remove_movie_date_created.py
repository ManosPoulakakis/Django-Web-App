# Generated by Django 2.1 on 2024-03-17 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='date_created',
        ),
    ]

# Generated by Django 2.2.12 on 2022-09-18 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_actor_director_movie_actor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_actor',
            name='actor_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='movie_actor',
            name='movie_id',
            field=models.IntegerField(default=0),
        ),
    ]

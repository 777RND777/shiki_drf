# Generated by Django 4.1.4 on 2023-01-06 09:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, unique=True)),
                ('slug', models.SlugField(max_length=500)),
                ('type_anime', models.CharField(choices=[('tv', 'Tv Series'), ('movie', 'Movie'), ('ova', 'Ova'), ('ona', 'Ona'), ('special', 'Special'), ('music', 'Music')], max_length=50)),
                ('episodes', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('status', models.CharField(choices=[('planned', 'Planned'), ('airing', 'Airing'), ('released', 'Released')], max_length=50)),
                ('score', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('synopsis', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['score'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('planned', 'Planned To Watch'), ('watching', 'Watching'), ('rewatching', 'Rewatching'), ('completed', 'Completed'), ('on_hold', 'On Hold'), ('dropped', 'Dropped')], max_length=50)),
                ('watched_episodes', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('text', models.TextField(blank=True)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.anime')),
            ],
        ),
    ]

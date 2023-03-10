# Generated by Django 4.1.4 on 2023-01-08 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='anime',
            name='genres',
            field=models.ManyToManyField(blank=True, to='anime.genre'),
        ),
        migrations.AddField(
            model_name='anime',
            name='studio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.studio'),
        ),
    ]

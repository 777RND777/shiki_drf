# Generated by Django 4.1.4 on 2023-01-05 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0007_alter_anime_score_alter_review_value'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='value',
            new_name='score',
        ),
    ]

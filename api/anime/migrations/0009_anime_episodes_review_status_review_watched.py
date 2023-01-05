# Generated by Django 4.1.4 on 2023-01-05 16:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0008_rename_value_review_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='episodes',
            field=models.IntegerField(default=13),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Dropped', 'Dropped'), ('On hold', 'On Hold'), ('Re-watching', 'Re Watching'), ('Watching', 'Watching')], default='Completed', max_length=50),
        ),
        migrations.AddField(
            model_name='review',
            name='watched',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]

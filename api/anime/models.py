from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify

from users.models import User

score_validator = [MaxValueValidator(10), MinValueValidator(1)]


class Genre(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Anime(models.Model):
    title = models.CharField(max_length=500, unique=True)
    slug = models.SlugField(max_length=500)
    score = models.FloatField(default=0, validators=score_validator)
    genres = models.ManyToManyField(Genre, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['score']


class Review(models.Model):
    value = models.IntegerField(validators=score_validator)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True)

    def __str__(self):
        return f"{self.value} for {self.anime} from {self.user}"

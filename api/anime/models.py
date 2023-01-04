from django.contrib.auth.models import AbstractUser
from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.title


class Anime(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500)
    score = models.FloatField(default=0)
    genres = models.ManyToManyField(Genre, blank=True)

    def __str__(self):
        return self.title


class User(AbstractUser):
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.username


class Review(models.Model):
    value = models.IntegerField(null=False)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True)

    def __str__(self):
        return f"{self.value} for {self.anime} from {self.user}"

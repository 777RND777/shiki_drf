from django.db import models

from users.models import User


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


class Review(models.Model):
    value = models.IntegerField(null=False)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True)

    def __str__(self):
        return f"{self.value} for {self.anime} from {self.user}"

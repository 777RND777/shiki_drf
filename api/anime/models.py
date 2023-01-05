from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify

from users.models import User

score_validator = [MinValueValidator(0), MaxValueValidator(10)]


class Genre(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Anime(models.Model):
    title = models.CharField(max_length=500, unique=True)
    slug = models.SlugField(max_length=500)
    episodes = models.IntegerField(validators=[MinValueValidator(0)])
    score = models.FloatField(validators=score_validator, default=0)
    genres = models.ManyToManyField(Genre, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['score']


class Review(models.Model):
    class Status(models.TextChoices):
        PLANNED_TO_WATCH = "planned"
        WATCHING = "watching"
        REWATCHING = "rewatching"
        COMPLETED = "completed"
        ON_HOLD = "on_hold"
        DROPPED = "dropped"

    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.COMPLETED)
    watched_episodes = models.IntegerField(default=0)
    score = models.IntegerField(validators=score_validator, default=0)
    text = models.TextField(blank=True)

    def __str__(self):
        return f"{self.score} for {self.anime} from {self.user}"

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import User

score_validator = [MinValueValidator(0), MaxValueValidator(10)]


class Genre(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.name


class Studio(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.name


class Anime(models.Model):
    class Kind(models.TextChoices):
        TV_SERIES = 'tv'
        MOVIE = 'movie'
        OVA = 'ova'
        ONA = 'ona'
        SPECIAL = 'special'
        MUSIC = 'music'

    class Status(models.TextChoices):
        ANNOUNCED = 'anons'
        AIRING = 'ongoing'
        FINISHED = 'released'

    title = models.CharField(max_length=500, unique=True)
    slug = models.SlugField(max_length=500)
    kind = models.CharField(max_length=50, choices=Kind.choices)
    episodes = models.IntegerField(validators=[MinValueValidator(0)])
    status = models.CharField(max_length=50, choices=Status.choices)
    genres = models.ManyToManyField(Genre, blank=True)
    score = models.FloatField(validators=score_validator, default=0)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    synopsis = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['score']


class Review(models.Model):
    class Status(models.TextChoices):
        PLANNED_TO_WATCH = 'planned'
        WATCHING = 'watching'
        REWATCHING = 'rewatching'
        COMPLETED = 'completed'
        ON_HOLD = 'on_hold'
        DROPPED = 'dropped'

    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=Status.choices)
    watched_episodes = models.IntegerField(default=0)
    score = models.IntegerField(validators=score_validator, default=0)
    text = models.TextField(blank=True)

    def __str__(self):
        return f'{self.score} for {self.anime} from {self.user}'

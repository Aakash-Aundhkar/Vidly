from django.db import models
from django.utils import timezone

# Create your models here.


class genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(genre, on_delete=models.CASCADE)
    datecreated = models.DateTimeField(default=timezone.now)

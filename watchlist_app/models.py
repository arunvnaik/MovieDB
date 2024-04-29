from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    name = models.CharField(max_length=100)
    year_of_release = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    rating = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='directors')

    def __str__(self):
        return self.name

class MovieActor(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='actors')

    def __str__(self):
        return self.name

class Technician(models.Model):
    name = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='technicians')
    field_of_work = models.CharField(max_length=100)

    def __str__(self):
        return self.name

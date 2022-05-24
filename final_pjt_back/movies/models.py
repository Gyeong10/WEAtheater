from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Actor(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    overview = models.TextField()
    movie_id = models.IntegerField()
    popularity = models.FloatField()
    vote_average = models.FloatField()
    poster_url = models.TextField()
    actors = models.ManyToManyField(Actor, related_name='movies')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    context = models.TextField(max_length=100)
    score = models.FloatField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
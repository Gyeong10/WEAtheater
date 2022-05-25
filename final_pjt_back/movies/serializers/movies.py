from rest_framework import serializers
from ..models import Movie, Genre, Actor
from django.contrib.auth import get_user_model
from .reviews import ReviewSerializer

User = get_user_model()

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('pk', 'name')

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('pk', 'name')
        
class MovieSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username',)

    genres = GenreSerializer(many=True, read_only=True)
    like_users = UserSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ('pk','title', 'release_date', 'genres', 'overview', 'movie_id', 'popularity', 'vote_average', 'poster_url', 'actors', 'like_users', 'reviews')
from movies.models import Movie
from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.models import Article
# from movies.models import Movie
class ProfileSerializer(serializers.ModelSerializer):
  
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('pk', 'title', 'content')

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('pk', 'poster_url', 'title')

    like_articles = ArticleSerializer(many=True, read_only=True)
    articles = ArticleSerializer(many=True, read_only=True)
    like_movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'articles', 'comments', 'like_articles', 'like_movies') #  'like_movies',
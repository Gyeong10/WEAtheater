from movies.models import Movie
from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.models import Article
from community.models import Comment


class ProfileSerializer(serializers.ModelSerializer):
  
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('pk', 'title', 'content', 'created_at', 'updated_at')

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('pk', 'poster_url', 'title')

    like_articles = ArticleSerializer(many=True, read_only=True)
    articles = ArticleSerializer(many=True, read_only=True)
    like_movies = MovieSerializer(many=True, read_only=True)

    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields =('pk', 'content', 'article', 'created_at', 'updated_at')

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'articles', 'comments', 'like_articles', 'like_movies') #  'like_movies',
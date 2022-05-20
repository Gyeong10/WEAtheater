from rest_framework import serializers
from django.contrib.auth import get_user_model
from .comment import CommentSerializer
from ..models import Article

User = get_user_model()

class ArticleSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username',)

    user = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    like_users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = ('pk', 'user', 'title', 'content', 'created_at', 'updated_at', 'like_users', 'comments',)

class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username',)
            
    user = UserSerializer(read_only=True)
    like_count = serializers.IntegerField()
    comment_count = serializers.IntegerField()

    class Meta:
      model = Article
      fields = ('pk', 'user', 'title', 'updated_at', 'like_count', 'comment_count',)
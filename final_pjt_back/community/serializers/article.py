from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Article

User = get_user_model()

class ArticleSerializer(serializers.ModelSerializer):
  class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ('pk', 'username',)
  # 아직 작성중
  class Meta:
    model = Article
    fields = ('pk', 'user', 'title', 'content',)
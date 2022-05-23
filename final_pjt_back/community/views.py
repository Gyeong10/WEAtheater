from tkinter import getboolean
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Count

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Article, Comment, Category
from .serializers.article import ArticleListSerializer, ArticleSerializer
from .serializers.comment import CommentSerializer
from django.forms.models import model_to_dict

# article 목록 조회, 생성
@api_view(['GET', 'POST'])
def article_list_or_create(request):

    def article_list():
        # commet 개수와 like 개수를 annotate로 추가하고 -pk로 정렬
        articles = Article.objects.annotate(
              comment_count=Count('comments', distinct=True),
              like_count=Count('like_users', distinct=True)
          ).order_by('-pk')
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    def article_create():
        category = get_object_or_404(Category, pk=request.data['category'])
        # print(f'request.data : {request.data}')
        # print(f'category: {category}')
        # cate_serializer = CategorySerializer(category)
        # print(cate_serializer.data)
        # data = request.data
        # data['category'] = cate_serializer.data
        # serializer = ArticleSerializer(data=request.data)
        serializer = ArticleSerializer(data=request.data)
        # print(serializer)
        # print(serializer.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, category=category)
            # print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return article_list()
    elif request.method == 'POST':
        return article_create()


# article 상세조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_or_update_or_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    def article_detail():
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def article_update():
        if article.user == request.user:
            serializer = ArticleSerializer(instance=article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
    
    def article_delete():
        if article.user == request.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return article_detail()
    elif request.method == 'PUT':
        return article_update()
    elif request.method == 'DELETE':
        return article_delete()


# 게시글 좋아요 기능
@api_view(['POST'])
def article_like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user
    if article.like_users.filter(pk=user.pk).exists():
      # 좋아요 취소
        article.like_users.remove(user)
    else:
      # 좋아요
        article.like_users.add(user)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)


# 댓글 작성
@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=article)
        # 댓글 추가 후 전체 댓글을 Response로 리턴해주어야 댓글 목록이 나옴
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 댓글 수정, 삭제
@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    def comment_update():
        if comment.user == request.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                # comment 수정 후 comment 목록을 불러와 Response로 리턴
                comments = article.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)
    def comment_delete():
        if comment.user == request.user:
            comment.delete()
            # comment 삭제 후 comment 목록을 불러와 Response로 리턴
            comments = article.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

    if request.method == 'PUT':
        return comment_update()
    elif request.method == 'DELETE':
        return comment_delete()
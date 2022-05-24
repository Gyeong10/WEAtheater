# from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from .models import Movie, Genre, Review
from .serializers.movies import MovieSerializer
from .serializers.reviews import ReviewSerializer

import requests
import json
import random
from django.forms.models import model_to_dict

# obj -> dict
def convert(ob):
    # user object -> dict
    now_movie = model_to_dict(ob)
    tmp = []
    for like_user in now_movie['like_users']:
        now_user = model_to_dict(like_user)
        tmp.append(now_user)
    now_movie['like_users'] = tmp

    # 배우 object -> dict
    tmp = []
    for actor in now_movie['actors']:
        now_actor = model_to_dict(actor)
        tmp.append(now_actor)
    now_movie['actors'] = tmp

    # 장르 object -> model
    temp = []
    for genr in now_movie['genres']:
        now_genre = model_to_dict(genr)
        temp.append(now_genre)
    now_movie['genres'] = temp
    return now_movie


# 장르별 영화 추천 알고리즘
def genre_recommend(request):
    user = request.user
    like_movies = user.like_movies.all()
    movie_list = []
    # 같은 장르 출력할 때 좋아요 누른 영화는 제외하고 추천하기 위해
    # 좋아요 누른 영화 id를 저장해놓았다가 id가 다른 영화만 list에 저장해서 출력
    ids = []
    for movie in like_movies:
        ids.append(movie.id)

    for movie in like_movies:
        for movie_genre in movie.genres.all():                
            genre = get_object_or_404(Genre, pk=movie_genre.id)
            genre_movies = genre.movies.all()[:6]
            for genre_movie in genre_movies:
                if genre_movie.id not in ids:
                    movie_list.append(convert(genre_movie))
    return movie_list


# 날씨별 영화 추천 알고리즘
def weather_recommend():
    here_req = requests.get("http://www.geoplugin.net/json.gp")

    movies = []
    if (here_req.status_code != 200):
        # print("현재좌표를 불러올 수 없음")
        movies = Movie.objects.all()[:10]
        # serializer = MovieSerializer(movies, many=True)
    else:
        location = json.loads(here_req.text)
        crd = {"lat": str(location["geoplugin_latitude"]), "lng": str(location["geoplugin_longitude"])}
        apiKey = '4152eb8dd166c278267accb9d4314069'
        weather_req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={crd['lat']}&lon={crd['lng']}&appid={apiKey}").json()
        # 날씨별 장르 id list
        weather_genre = {
            'Thunderstrom': [80, 27, 53, 9648],
            'Drizzle': [16, 10402, 36],
            'Rain': [27, 9648, 53, 12],
            'Snow': [18, 10749, 10770, 10751],
            'Atmosphere': [9645, 10752, 818, 37],
            'Clear': [28, 12, 16, 35, 10751, 14],
            'Clouds': [36, 99, 10402]
        }
        weather_genre_list = weather_genre[weather_req['weather'][0]['main']]
        # print(crd)
        # print(weather_req['weather'])
        # print(weather_genre_list)
        # 장르 id로 genre object를 찾은 뒤 그 genre를 역참조하는 movies를 genre_movies에 할당
        # 그 영화들을 movies list에 추가한 뒤 리턴
        # cnt = 0
        for genre_pk in weather_genre_list:
            genre = get_object_or_404(Genre, pk=genre_pk)
            genre_movies = genre.movies.all()[:5]   # 장르별 영화 받아오기
            for genre_movie in genre_movies:
                movies.append(convert(genre_movie))
    return movies    

# 배우별 영화 추천 알고리즘
# 데이터가 없어서 확인 불가..
def actor_recommend(request):
    user = request.user
    rec_movies = []
    movie_list = user.like_movies.all()
    for movie in movie_list:
        now_movie = get_object_or_404(Movie, pk=movie.pk)
        actor_list = now_movie.actors.all()
        for actor in actor_list:
            ms = actor.movies.all()
            for m in ms:
                if m not in rec_movies:
                    rec_movies.append(convert(m))
    return rec_movies


@api_view(['GET'])
def movie_list(request):
    top10_list = Movie.objects.order_by('pk')[:10]
    top10 = []
    for top10_movie in top10_list:
        top10.append(convert(top10_movie))

    genre = genre_recommend(request)
    weather = weather_recommend()
    actor = actor_recommend(request)

    serializer = [
        {
        'top10': top10
        },
        {
        'actor': actor
        },
        {
        'weather': weather
        },
        {
        'genre': genre
        }
    ]
    return Response(serializer)


@api_view(['GET'])
def search(request, input):

    API_KEY = '734f0f8517f219408b7b36148ae92b32'
    
    search_result = requests.get(f'https://api.themoviedb.org/3/search/multi?api_key={API_KEY}&language=ko-KR&page=1&include_adult=false&query={input}').json()

    return Response(search_result)

@api_view(['GET'])
def all_movie_list(request):
    movies = Movie.objects.order_by('pk')
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def review_create(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)

        reviews = movie.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def review_update_or_delete(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)

    def review_update():
      if request.user == review.user:
          serializer = ReviewSerializer(instance=review, data=request.data)
          if serializer.is_valid(raise_exception=True):
              serializer.save()

              reviews = movie.reviews.all()
              serializer = ReviewSerializer(reviews, many=True)
              return Response(serializer.data)

    def review_delete():
        if request.user == review.user:
            review.delete()
            reviews = movie.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return review_update()
    elif request.method == 'DELETE':
        return review_delete()


@api_view(['POST'])
def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        
    else:
        movie.like_users.add(user)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def review_like(request, review_pk):
    review = get_object_or_404(Movie, pk=review_pk)
    user = request.user
    if review.like_users.filter(pk=user.pk).exists():
        review.like_users.remove(user)
    else:
        review.like_users.add(user)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)

@api_view(['GET'])
def review_list(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews = movie.reviews.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

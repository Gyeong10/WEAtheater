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

# 장르별 영화 추천 알고리즘
def genre_recommend(user):
    like_movies = user.like_movies.all()
    movie_list = []
    # 같은 장르 출력할 때 좋아요 누른 영화는 제외하고 추천하기 위해
    # 좋아요 누른 영화 id를 저장해놓았다가 id가 다른 영화만 list에 저장해서 출력
    ids = []
    for movie in like_movies:
        ids.append(movie['id'])
    # print(ids)

    for movie in like_movies:
        for movie_genre in movie['genres']:                
            genre = get_object_or_404(Genre, pk=movie_genre)
            genre_movies = genre.movies.all()
            for genre_movie in genre_movies:
                # print(genre_movie.title)
                if genre_movie.id not in ids:
                    movie_list.append(genre_movie)
    serializer = MovieSerializer(movie_list, many=True)
    # return movie_list
    return Response(serializer.data)
            


# 날씨별 영화 추천 알고리즘
def weather_recommend():
    here_req = requests.get("http://www.geoplugin.net/json.gp")

    movies = []
    if (here_req.status_code != 200):
        # print("현재좌표를 불러올 수 없음")
        movies = Movie.objects.all()[:10]
        serializer = MovieSerializer(movies, many=True)
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
        for genre_pk in weather_genre_list:
            genre = get_object_or_404(Genre, pk=genre_pk)
            genre_movies = genre.movies.all()
            for genre_movie in genre_movies:
                movies.append(genre_movie)
        serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
        

# 배우별 영화 추천 알고리즘
# 데이터가 없어서 확인 불가..
def actor_recommend(request):

    API_KEY = '734f0f8517f219408b7b36148ae92b32'

    user = request.user
    actor_list = []
    movies = user.like_movies.all()
    for movie in movies:
        if user.pk == movie['user_id']:
            movie_id = movie['movie_id']
            movie_details = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}&language=en-US').json()
            for movie_detail in movie_details['cast']:
                if movie_detail['Konwn_for_department'] == 'Acting' and movie_detail['popularity'] >= 10:
                    actor_list.append(movie_detail['id'])

    actor_movie_id = []
    for actor_pk in actor_list:
        actor_movies = requests.get(f'https://api.themoviedb.org/3/person/{actor_pk}/movie_credits?api_key={API_KEY}&language=en-US').json()
        for movie in actor_movies['cast']:
            if movie['popularity'] >= 10:
                actor_movie_id.append(movie['id'])
    
    actor_movie_list = []
    for movie_id in actor_movie_id:
        actor_movie = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=ko-KR').json()
        movie_set = {
            'title': actor_movie['title'],
            'release_date': actor_movie['release_date'],
            'genres': actor_movie['genres'],
            'overview': actor_movie['overview'],
            'movie_id': actor_movie['movie_id'],
            'popularity': actor_movie['popularity'],
            'vote_average': actor_movie['vote_average'],
            'poster_url': actor_movie['poster_url']
        }
        actor_movie_list.append(movie_set)
    
    return Response()


@api_view(['GET'])
def movie_list(request):
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


@api_view(['DELETE'])
def review_delete(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)

    if request.user == review.user:
        review.delete()
        reviews = movie.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
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
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    else:
        review.like_users.add(user)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
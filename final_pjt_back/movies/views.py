# from django.http import JsonResponse
from unittest import result
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

# 장르별 영화 추천 알고리즘
def genre_recommend(user):
    like_movies = user.like_movies.all()
    movie_list = []
    # 같은 장르 출력할 때 좋아요 누른 영화는 제외하고 추천하기 위해
    # 좋아요 누른 영화 id를 저장해놓았다가 id가 다른 영화만 list에 저장해서 출력
    ids = []
    for movie in like_movies:
        ids.append(movie.id)
    # print(ids)
    cnt = 0
    flag = 0
    for movie in like_movies:
        for movie_genre in movie.genres.all():                
            genre = get_object_or_404(Genre, pk=movie_genre.id)
            genre_movies = genre.movies.all()
            for genre_movie in genre_movies:
                # print(json.load(genre_movie))
                if genre_movie.id not in ids:
                    # file = open(f"{genre_movie}.json", "r", encoding='utf-8')
                    movie_dict = model_to_dict(genre_movie)
                    genres = []
                    for g in movie_dict['genres']:
                        # print(model_to_dict(g))
                        genres.append(model_to_dict(g)['id'])
                    # print(genres)
                    movie_dict['genres'] = genres
                    movie_list.append(movie_dict)
                    cnt += 1
                if cnt == 10:
                    return movie_list
    #                 flag = 1
    #                 break
    #         if flag:
    #           break
    #     if flag:
    #       break

    # serializer = MovieSerializer(movie_list, many=True)
    # return Response(serializer.data)
            


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
        cnt = 0
        for genre_pk in weather_genre_list:
            genre = get_object_or_404(Genre, pk=genre_pk)
            genre_movies = genre.movies.all()
            for genre_movie in genre_movies:
                # file = open(f"{genre_movie}.json", "r", encoding='utf-8')
                # movies.append(model_to_dict(genre_movie))
                # print(model_to_dict(genre_movie)['genres'])
                dict_movie = model_to_dict(genre_movie) 

                temp = []
                for genr in dict_movie['genres']:
                    temp.append(model_to_dict(genr)['id'])
                dict_movie['genres'] = temp
                movies.append(dict_movie)

                cnt += 1
            if cnt >= 10:
                break
    #     serializer = MovieSerializer(movies, many=True)
    # return Response(serializer.data)
    return movies    

# 배우별 영화 추천 알고리즘
# 데이터가 없어서 확인 불가..
def actor_recommend(request):

    API_KEY = '734f0f8517f219408b7b36148ae92b32'

    user = request.user
    actor_list = []
    movies = user.like_movies.all()
    # print(movies)
    for movie in movies:
        
        # if user.pk == movie['user_id']:
        movie_id = movie.movie_id
        # movie_id = movie['movie_id']
        movie_details = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}&language=ko-KR').json()
        for movie_detail in movie_details['cast']:
            # print(movie_detail)
            if movie_detail['known_for_department'] == 'Acting' and movie_detail['popularity'] >= 10:
                actor_list.append(movie_detail['id'])

    actor_movie_id = []
    for actor_pk in actor_list:
        actor_movies = requests.get(f'https://api.themoviedb.org/3/person/{actor_pk}/movie_credits?api_key={API_KEY}&language=ko-KR').json()
        for movie in actor_movies['cast']:
            if movie['popularity'] >= 10:
                actor_movie_id.append(movie['id'])
    cnt = 0
    actor_movie_list = []
    for movie_id in actor_movie_id:
        actor_movie = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=ko-KR').json()
        genres = []
        for genre in actor_movie['genres']:
            genres.append(genre['id'])
        movie_set = {
            'title': actor_movie['title'],
            'release_date': actor_movie['release_date'],
            # 'genres': actor_movie['genres'], # 여기서 장르가 숫자로 안들어오고 Genre object로 들어와서 오류
            'genres': genres,
            'overview': actor_movie['overview'],
            'movie_id': actor_movie['id'],
            'popularity': actor_movie['popularity'],
            'vote_average': actor_movie['vote_average'],
            'poster_url': actor_movie['poster_path']
        }
        actor_movie_list.append(movie_set)
        cnt += 1
        if cnt == 10:
            break
    # results = MovieSerializer(actor_movie_list, many=True)
    # return Response()
    return actor_movie_list


@api_view(['GET'])
def movie_list(request):
    # print(f'genre: {genre_recommend(request.user)}')
    movies = Movie.objects.order_by('pk')[:10]
    serializer = MovieSerializer(movies, many=True)
    top10_list = Movie.objects.order_by('pk')[:10]
    # top10_list = MovieSerializer(top10movies, many=True)
    top10 = []
    # print(top10_list)
    for top10_movie in top10_list:
        file = model_to_dict(top10_movie)
        genres = []
        for genre in file['genres']:
            genres.append(model_to_dict(genre)['id'])
        file['genres'] = genres
        top10.append(file)

    # print(f'top10: {top10}')
    # print(f'weather: {weather_recommend()}')
    # print(f'actor: {actor_recommend(request)}')

    genre = genre_recommend(request.user)
    weather = weather_recommend()
    actor = actor_recommend(request)
    # print(genre)

    # TypeError: Object of type User is not JSON serializable
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

    # return Response(serializer.data)


def search(request):

    API_KEY = '734f0f8517f219408b7b36148ae92b32'
    
    search_result = requests.get(f'https://api.themoviedb.org/3/search/multi?api_key={API_KEY}&language=ko-KR&page=1&include_adult=false&query={request.data}')

    return Response(search_result)




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
      if request.uer == review.user:
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
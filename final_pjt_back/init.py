import requests
import json

TMDB_API_KEY = '734f0f8517f219408b7b36148ae92b32'

all_actors = set()

def get_movie_datas():
    total_data = []
    num = 1
    movie_id = 0
    for i in range(1, 2000):
        movies_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(movies_url).json()
        details_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=ko-KR'
        for movie in movies['results']:
            movie_id = movie['id']
            movie_details = requests.get(details_url).json()
            actor_list = []
            if 'cast' in movie_details.keys():
                for person in movie_details['cast']:
                    cnt = 0
                    if cnt <= 5:
                        if person['known_for_department'] == 'Acting' and person['popularity'] >= 10:
                            actor_list.append(person['id'])
                            all_actors.add((person['id'], person['name']))
                            cnt += 1
                    else:
                        break
            if movie.get('release_date', ''):
                fields = {
                    'movie_id': movie['id'],
                    'title': movie['title'],
                    'release_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_average': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_url': movie['poster_path'],
                    'genres': movie['genre_ids'],
                    'actors' : actor_list,
                }

                data = {
                    "pk": num,
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)
            num += 1

    with open("movies/fixtures/movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)

def get_genre_data():
    total_data = []

    request_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}"
    genres = requests.get(request_url).json()

    for genre in genres['genres']:
        fields = {
            # 'genre_id': genre['id'],
            'name': genre['name'],
        }

        data = {
            "pk": genre['id'],
            "model": "movies.genre",
            "fields": fields
        }
        total_data.append(data)

    with open("movies/fixtures/genre_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)


def get_actor_data():
    global all_actors
    total_data = []
    all_actors = list(all_actors)
    for actor in all_actors:
        fields = {
            'name': actor[1],
        }

        data = {
            "pk": actor[0],
            "model": "movies.actor",
            "fields": fields
        }
        total_data.append(data)
    
    with open("movies/fixtures/actor_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)

get_movie_datas()
get_genre_data()
get_actor_data()

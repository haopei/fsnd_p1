import fresh_tomatoes
import json
from model import Movie


# decode json data from movies.json
# see: http://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file-in-python
with open('movies.json') as data_file:
    movies_json = json.load(data_file)

# add Movie objects to 'movies' list
movies = []
for m in movies_json:
    movie = Movie(
        m['title'], m['story'],
        m['poster_image_url'],
        m['trailer_youtube_url'],
        m['duration'], m['genre'],
        m['year'])
    movies.append(movie)

# create/overwrite and open html page
fresh_tomatoes.open_movies_page(movies)

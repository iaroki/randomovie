import random
import tmdbsimple as tmdb
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    with open('api.key', 'r') as keyfile:
        apikey = keyfile.readline()

    tmdb.API_KEY = apikey

    genres = tmdb.Genres()
    response = genres.list()
    genredict = response['genres']
    mygenres = {}

    for dicts in genredict:
        for i in range(1):
            mygenres[dicts['name']] = dicts['id']

    return render_template('index.html', mygenres=mygenres)

@app.route('/Western')
def randoms():
    movies = tmdb.Genres(id=37)
#    pages = movies.movies()['total_pages']
#    data = movies.movies(page=random.randint(1, pages))
    rawdata = movies.movies()
    pages = rawdata['total_pages']
    data = rawdata['page']
    return render_template('random.html', data=data)

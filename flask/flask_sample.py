#!/usr/bin/env python3
'''
    flask_sample.py
    Jeff Ondich, 22 April 2016
    Updated 7 October 2020

    A slightly more complicated Flask sample app than the
    "hello world" app found at http://flask.pocoo.org/.
'''
import sys
import argparse
import flask
import json

app = flask.Flask(__name__)

# Who needs a database when you can just hard-code some actors and movies?
actors = [
    {'last_name': 'Pickford', 'first_name': 'Mary', 'birth_year':1892, 'death_year':1979},
    {'last_name': 'Rains', 'first_name': 'Claude', 'birth_year':1889, 'death_year':1967},
    {'last_name': 'Lorre', 'first_name': 'Peter', 'birth_year':1904, 'death_year':1964},
    {'last_name': 'Greenstreet', 'first_name': 'Sydney', 'birth_year':1879, 'death_year':1954},
    {'last_name': 'Bergman', 'first_name': 'Ingrid', 'birth_year':1915, 'death_year':1982},
    {'last_name': 'Grant', 'first_name': 'Cary', 'birth_year':1904, 'death_year':1986},
    {'last_name': 'Colbert', 'first_name': 'Claudette', 'birth_year':1903, 'death_year':1996},
    {'last_name': 'McDormand', 'first_name': 'Frances', 'birth_year':1957, 'death_year':None},
    {'last_name': 'Thompson', 'first_name': 'Tessa', 'birth_year':1983, 'death_year':None},
    {'last_name': 'Wiig', 'first_name': 'Kristen', 'birth_year':1973, 'death_year':None},
    {'last_name': 'Adams', 'first_name': 'Amy', 'birth_year':1974, 'death_year':None}
]

movies = [
    {'title': 'Casablanca', 'year': 1942, 'genre': 'drama'},
    {'title': 'North By Northwest', 'year': 1959, 'genre': 'thriller'},
    {'title': 'Alien', 'year': 1979, 'genre': 'scifi'},
    {'title': 'Bridesmaids', 'year': 2011, 'genre': 'comedy'},
    {'title': 'Arrival', 'year': 2016, 'genre': 'scifi'},
    {'title': 'Booksmart', 'year': 2019, 'genre': 'comedy'},
    {'title': 'It Happened One Night', 'year': 1934, 'genre': 'comedy'},
    {'title': 'Fargo', 'year': 1996, 'genre': 'thriller'},
    {'title': 'Sorry to Bother You', 'year': 2018, 'genre': 'comedy'},
    {'title': 'Passing', 'year': 2021, 'genre': 'drama'},
    {'title': 'Clueless', 'year': 1995, 'genre': 'comedy'}
]

@app.route('/')
def hello():
    return 'Hello, Citizen of CS257.'

@app.route('/actor/<last_name>')
def get_actor(last_name):
    ''' Returns the first matching actor, or an empty dictionary if there's no match. '''
    actor_dictionary = {}
    lower_last_name = last_name.lower()
    for actor in actors:
        if actor['last_name'].lower().startswith(lower_last_name):
            actor_dictionary = actor
            break
    return json.dumps(actor_dictionary)

@app.route('/movies')
def get_movies():
    ''' Returns the list of movies that match GET parameters:
          start_year, int: reject any movie released earlier than this year
          end_year, int: reject any movie released later than this year
          genre: reject any movie whose genre does not match this genre exactly
        If a GET parameter is absent, then any movie is treated as though
        it meets the corresponding constraint. (That is, accept a movie unless
        it is explicitly rejected by a GET parameter.)
    '''
    movie_list = []
    genre = flask.request.args.get('genre')
    start_year = flask.request.args.get('start_year', default=0, type=int)
    end_year = flask.request.args.get('end_year', default=10000, type=int)
    for movie in movies:
        if genre is not None and genre != movie['genre']:
            continue
        if movie['year'] < start_year:
            continue
        if movie['year'] > end_year:
            continue
        movie_list.append(movie)

    return json.dumps(movie_list)

@app.route('/help')
def get_help():
    return flask.render_template('help.html')

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A sample Flask application/API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)

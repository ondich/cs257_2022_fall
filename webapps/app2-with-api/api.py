'''
    app.py
    Jeff Ondich, 25 April 2016
    Updated 5 November 2021

    Tiny Flask API to support a cats and dogs web application
    that doesn't use a database.
'''
import flask
import json

api = flask.Blueprint('api', __name__)

# Of course, your API will be extracting data from your postgresql database.
# To keep the structure of this tiny API crystal-clear, I'm just hard-coding data here.
cats = [{'name':'Emma', 'birth_year':1983, 'death_year':2003, 'description':'the boss'},
        {'name':'Aleph', 'birth_year':1984, 'death_year':2002, 'description':'sweet and cranky'},
        {'name':'Curby', 'birth_year':1999, 'death_year':2000, 'description':'gone too soon'},
        {'name':'Digby', 'birth_year':2000, 'death_year':2018, 'description':'the epitome of Cat'},
        {'name':'Max', 'birth_year':1998, 'death_year':2009, 'description':'seismic'},
        {'name':'Scout', 'birth_year':2007, 'death_year':None, 'description':'accident-prone'}]

dogs = [{'name':'Ruby', 'birth_year':2003, 'death_year':2016, 'description':'a very good dog'},
        {'name':'Maisie', 'birth_year':2017, 'death_year':None, 'description':'a very good dog'}]

@api.route('/cats/', strict_slashes=False)
def get_cats():
    return json.dumps(cats)

@api.route('/dogs/')#, strict_slashes=False) 
def get_dogs():
    return json.dumps(dogs)


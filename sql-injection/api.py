'''
    api.py
    Jeff Ondich, 13 November 2020

    Tiny books/authors API to help illustrate SQL Injection
'''
import sys
import flask
import json
import config
import psycopg2

api = flask.Blueprint('api', __name__)

## THIS ROUTE IS BAD!! ##
@api.route('/authors/dangerous/<search_text>')
def get_authors_dangerously(search_text):
    # Yikes! Here's where the injection happens. We're sticking
    # user-generated content (search_text) directly into our SQL query.
    # Don't do this!
    query = f''' SELECT given_name, surname
                 FROM authors
                 WHERE surname LIKE '%{search_text}%' '''

    author_list = []
    try:
        connection = psycopg2.connect(database=config.database,
                                      user=config.user,
                                      password=config.password)
        cursor = connection.cursor()
        cursor.execute(query) # Always be suspicious of the 1-parameter cursor.execute.
        print('QUERY:', cursor.query.decode('utf-8'))
        for row in cursor:
            author = {'given_name':row[0], 'surname':row[1]}
            author_list.append(author)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(author_list)

# This route fixes the problem demonstrated in the previous route. I don't
# think it introduces new problems in the process, but please let me know if it does!
@api.route('/authors/<search_text>')
def get_authors_less_dangerously(search_text):
    like_argument = '%' + search_text + '%' # 1. isolate the user input
    query = ''' SELECT given_name, surname
                FROM authors
                WHERE surname LIKE %s ''' # 2. put a placeholder for the user input here

    author_list = []
    try:
        connection = psycopg2.connect(database=config.database,
                                      user=config.user,
                                      password=config.password)
        cursor = connection.cursor()
        cursor.execute(query, (like_argument,)) # 3. Let cursor.execute sanitize the user input
        print('QUERY:', cursor.query.decode('utf-8'))
        for row in cursor:
            author = {'given_name':row[0], 'surname':row[1]}
            author_list.append(author)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(author_list)


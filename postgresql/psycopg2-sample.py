#!/usr/bin/env python3
'''
    psycopg2-sample.py
    Jeff Ondich, 23 April 2016

    A very short, demo of how to use psycopg2 to connect to
    and query a PostgreSQL database. This demo assumes a "books"
    database like the one I've used in CS257 for the past few years,
    including an authors table with fields

        (id, given_name, surname, birth_year, death_year)

    You might also want to consult the official psycopg2 tutorial
    at https://wiki.postgresql.org/wiki/Psycopg2_Tutorial.

    Also, SEE THE NOTE BELOW ABOUT config.py. It's important.
'''
import sys
import psycopg2

# We're also going to import our postgres username, password,
# and database from a file named config.py, like so:
import config

# Here are steps you should take to make this "import config" work properly.
#
# 1. DO THIS IMMEDIATELY, DON'T WAIT! Create a .gitignore file in the
#    directory containing your python program (I've already done so for this
#    sample directory). Your .gitignore file should contain this line:
#
#     config.py
#
# 2. Create a config.py file in this directory, containing three
#    assignment statements:
#
#     database = 'YOUR_DATABASE_NAME'  (whatever your database name is, like 'books')
#     user = 'YOUR_POSTGRES_USER_NAME'
#     password = 'YOUR_POSTGRES_PASSWORD_IF_ANY'
#
# 3. That's it, congratulations! You have now made your postgres login information
#    available to your python program, but you've prevented that information from
#    getting accidentally pushed to your git repository. Keeping your login info
#    out of your public repos (or your private ones, for that matter) will go a long
#    way towards avoiding one of the most obvious and bone-headed security problems.
#

def get_connection():
    ''' Returns a database connection object with which you can create cursors,
        issue SQL queries, etc. This function is extremely aggressive about
        failed connections--it just prints an error message and kills the whole
        program. Sometimes that's the right choice, but it depends on your
        error-handling needs. '''
    try:
        return psycopg2.connect(database=config.database,
                                user=config.user,
                                password=config.password)
    except Exception as e:
        print(e, file=sys.stderr)
        exit()

def get_authors():
    ''' Returns a list of the full names of all the authors
        in the database, ordered by surname. '''
    authors = []
    try:
        # Create a "cursor", which is an object with which you can iterate
        # over query results.
        connection = get_connection()
        cursor = connection.cursor()

        # Execute the query
        query = 'SELECT given_name, surname FROM authors ORDER BY surname'
        cursor.execute(query)

        # Iterate over the query results to produce the list of author names.
        for row in cursor:
            given_name = row[0]
            surname = row[1]
            authors.append(f'{given_name} {surname}')

    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return authors

def get_authors_by_surname(search_text):
    ''' Returns a list of the full names of all authors in the database
        whose surnames are equal to the specified search string.

        This function introduces an important security issue. Suppose you
        have information provided by your user (e.g. a search string)
        that needs to become part of your SQL query. Since you can't trust
        users not to be malicious, nor can you trust them not to do weird and
        accidentally destructive things, you need to be very careful about
        how you use any input they provide. To avoid the very common and
        very dangerous security attack known as "SQL Injection", we will use
        the parameterized version of cursor.execute whenever we're using
        user-generated data. See below for how that goes. '''
    authors = []
    try:
        query = '''SELECT given_name, surname
                   FROM authors
                   WHERE surname = %s'''
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (search_text,))
        for row in cursor:
            given_name = row[0]
            surname = row[1]
            authors.append(f'{given_name} {surname}')

    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return authors

def get_matching_authors(search_text):
    ''' Returns a list of the full names of all authors in the database
        whose surnames contain (case-insensitively) the specified search string. '''
    authors = []
    try:
        query = '''SELECT given_name, surname
                   FROM authors
                   WHERE surname ILIKE CONCAT('%%', %s, '%%')'''
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (search_text,))
        for row in cursor:
            given_name = row[0]
            surname = row[1]
            authors.append(f'{given_name} {surname}')

    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return authors


def main():
    # Example #1: get a list of author names
    print('========== All authors ==========')
    authors = get_authors()
    for author in authors:
        print(author)
    print()

    # Example #2: get a list of authors whose surnames equal a search string
    surname = 'Brontë'
    print(f'========== All authors with surname "{surname}" ==========')
    authors = get_authors_by_surname(surname)
    for author in authors:
        print(author)
    print()

    # Example #3: get a list of authors whose surnames contain a search string
    search_text = 'is'
    print(f'========== All authors whose surnames contain "{search_text}" ==========')
    authors = get_matching_authors(search_text)
    for author in authors:
        print(author)
    print()



if __name__ == '__main__':
    main()


#!/usr/bin/env python3
'''
    app.py
    Jeff Ondich
    Updated: 5 November 2021

    A tiny Flask web application, including API, to be used
    as a template for setting up your web app assignment.
'''
import argparse
import flask

app = flask.Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return flask.render_template('index.html', user_name='Jeff')

@app.route('/about')
def about():
    return flask.render_template('about.html')


if __name__ == '__main__':
    parser = argparse.ArgumentParser('A tiny Flask application with no API')
    parser.add_argument('host', help='the host to run on')
    parser.add_argument('port', type=int, help='the port to listen on')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)


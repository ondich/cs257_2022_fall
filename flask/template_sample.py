#!/usr/bin/env python3
'''
    template_sample.py
    Jeff Ondich
    6 November 2020

    Using templates in Flask.
'''
import sys
import argparse
import flask
import json

app = flask.Flask(__name__)

@app.route('/')
def home():
    return flask.render_template('index.html')

@app.route('/hello/<name>')
def hello(name):
    return flask.render_template('hello.html', user_name=name)

@app.route('/shared-header/')
def shared_header():
    return flask.render_template('shared-header/index.html')

@app.route('/shared-header/<path:path>')
def shared_header_catchall(path):
    return flask.render_template('shared-header/' + path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A sample Flask application demonstrating templates.')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)

#!/usr/bin/env python3
'''
    covid-api-tester.py
    Jeff Ondich, 25 October 2021

    This is a demo of how to use a public API from
    a Python program. It's not intended to be particularly
    user-friendly or extensible. It just shows the minimum
    code required to extract a little data from the API at
    https://covidtracking.com/data/api.

    When I first tried to run this on macOS, I got an error
    telling me there was no file named ~/.ssl/output.log.
    So I did this:

        cd
        mkdir .ssl
        touch .ssl/output.log   [this just creates a 0-byte file]

    and everything worked fine after that.
'''

import sys
import json
import urllib.request

def print_state_death_counts(state):
    url = f'https://api.covidtracking.com/v1/states/{state}/daily.json'
    data_from_server = urllib.request.urlopen(url).read()
    string_from_server = data_from_server.decode('utf-8')
    covid_day_list = json.loads(string_from_server)

    for covid_day in covid_day_list:
        print(covid_day['date'], covid_day['deathIncrease'])

print_state_death_counts('mn')


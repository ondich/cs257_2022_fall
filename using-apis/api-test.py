#!/usr/bin/env python3
'''
    api-test.py
    Jeff Ondich, 11 April 2016
    Updated 7 October 2020

    An example for CS 257 Software Design. How to retrieve results
    from an HTTP-based API, parse the results (JSON in this case),
    and manage the potential errors.
'''

import sys
import argparse
import json
import urllib.request

API_BASE_URL = 'http://api.ultralingua.com/api/2.0'
API_KEY = 'cs257'

def get_root_words(word, language):
    '''
    Returns a list of root words for the specified word in the
    specified language. The root words are represented as
    dictionaries of the form
    
       {'root':root_word, 'partofspeech':part_of_speech}

    For example, the results for get_root_words('thought', 'eng')
    would be:

       [{'root':'thought', 'partofspeech':'noun'},
        {'root':'think', 'partofspeech':'verb'}]

    The language parameter must be a 3-letter ISO language code
    (e.g. 'eng', 'fra', 'deu', 'spa', etc.).

    Raises exceptions on network connection errors and on data
    format errors.
    '''
    url = f'{API_BASE_URL}/stems/{language}/{word}?key={API_KEY}'
    data_from_server = urllib.request.urlopen(url).read()
    string_from_server = data_from_server.decode('utf-8')
    root_word_list = json.loads(string_from_server)
    result_list = []
    for root_word_dictionary in root_word_list:
        root = root_word_dictionary.get('text', '')
        part_of_speech = root_word_dictionary.get('partofspeech', {})
        part_of_speech_category = part_of_speech.get('partofspeechcategory', '')
        result_list.append({'root':root, 'partofspeech':part_of_speech_category})
    return result_list

def get_conjugations(verb, language):
    '''
    Returns a list of conjugations for the specified verb in the
    specified language. The conjugations are represented as
    dictionaries of the form
    
       {'text':..., 'tense':..., 'person':..., 'number':...}

    For example, the results for get_root_words('parler', 'fra')
    would include:

       [{'text':'parle', 'tense':'present', 'person':'first', 'number':'singular'},
        {'text':'parles', 'tense':'present', 'person':'second', 'number':'singular'},
        ...
       ]

    The language parameter must be a 3-letter ISO language code
    (e.g. 'eng', 'fra', 'deu', 'spa', etc.).

    Raises exceptions on network connection errors and on data
    format errors.
    '''
    url = f'{API_BASE_URL}/conjugations/{language}/{verb}?key={API_KEY}'
    data_from_server = urllib.request.urlopen(url).read()
    string_from_server = data_from_server.decode('utf-8')
    verbs = json.loads(string_from_server)

    result_list = []
    for verb in verbs:
        if 'conjugations' not in verb:
            print(f'Unexpected response format for {verb}', file=sys.stderr)
            continue
        for conjugation_dictionary in verb['conjugations']:
            text = conjugation_dictionary.get('surfaceform', '')
            part_of_speech = conjugation_dictionary.get('partofspeech', {})
            tense = part_of_speech.get('tense', '')
            person = part_of_speech.get('person', '')
            number = part_of_speech.get('number', '')
            result_list.append({'text':text, 'tense':tense, 'person':person, 'number':number})

    return result_list

def main(args):
    if args.action == 'root':
        root_words = get_root_words(args.word, args.language)
        for root_word in root_words:
            root = root_word['root']
            part_of_speech = root_word['partofspeech']
            print(f'{root} [{part_of_speech}]')

    elif args.action == 'conjugate':
        conjugations = get_conjugations(args.word, args.language)
        for conjugation in conjugations:
            text = conjugation['text']
            tense = conjugation['tense']
            person = conjugation['person']
            number = conjugation['number']
            print(f'{text} [{tense} {person} {number}]')
    
if __name__ == '__main__':
    # When I use argparse to parse my command line, I usually
    # put the argparse setup here in the global code, and then
    # call a function called main to do the actual work of
    # the program.
    parser = argparse.ArgumentParser(description='Get word info from the Ultralingua API')

    parser.add_argument('action',
                        metavar='action',
                        help='action to perform on the word ("root" or "conjugate")',
                        choices=['root', 'conjugate'])

    parser.add_argument('language',
                        metavar='language',
                        help='the language as a 3-character ISO code',
                        choices=['eng', 'fra', 'spa', 'deu', 'ita', 'por'])

    parser.add_argument('word', help='the word you want to act on')

    args = parser.parse_args()
    main(args)

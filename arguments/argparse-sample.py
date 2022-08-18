'''
    argparse_example.py
    Jeff Ondich
    3 October 2020

    Example of how to use the standard argparse module to 
    describe and parse a command-line interface.

    Try a few ways of using the arguments:

        python3 argparse_example.py cat
        python3 argparse_example.py --language spanish dog cat moose
        python3 argparse_example.py --language=spanish dog cat moose
        python3 argparse_example.py dog cat moose -l spanish
        python3 argparse_example.py dog cat moose -lfrench

    Notes:
    + the "options" (like --language and -l) can come either before or after the
        "positional" arguments (dog, cat, etc.)
    + a single-minus option can be used either with or without a space
        "-l french" or "-lfrench"
    + a double-minus option can be used either with a space or an equals sign
        "--language spanish" or "--language=spanish"
    + how do you think I managed to let it let me type in more than one
        animal at once?
'''

import argparse

def get_parsed_arguments():
    parser = argparse.ArgumentParser(description='Report on the vocalizations of animals.')
    parser.add_argument('animals', metavar='animal', nargs='+', help='one or more animals whose noises you seek')
    parser.add_argument('--language', '-l', default='english', help='the language in which the noises will be reported')
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def get_animal_noise(language, animal):
    noises = {'english': {'dog':'woof', 'cat':'meow', 'pig':'oink'},
              'french': {'dog':'ouaf', 'cat':'miaou', 'pig':'groin'},
              'spanish': {'dog':'guau', 'cat':'miau', 'pig':'oinc'}}

    animal_noise = ''
    language = language.lower()
    if language in noises:
        if animal in noises[language]:
            animal_noise = noises[language][animal]
    return animal_noise

def main():
    arguments = get_parsed_arguments()
    for animal in arguments.animals:
        noise = get_animal_noise(arguments.language, animal)
        if noise:
            print(f'The {animal} says "{noise}"')
        else:
            print(f'I don\'t know what the {animal} says in {arguments.language}')

if __name__ == '__main__':
    main()


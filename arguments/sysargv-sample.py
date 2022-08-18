'''
    sysargv-sample.py
    Jeff Ondich, 21 September 2020
    Updated, 18 August 2022

    A simple illustration of command-line parsing without using
    a library like argparse.
'''

import sys

def usage_statement():
    statement = f'Usage: {sys.argv[0]} person-name\n'
    statement += '    Prints a greeting to the named person.'
    return statement

def parse_command_line():
    ''' This, of course, would be a lot more complicated if we
        had a more complex command-line interface design. For this
        very simple program, however, all we care about is obtaining
        the person-name from the command line and saving it for
        use in the rest of the program. '''
    arguments = {}
    if len(sys.argv) == 2:
        arguments['person-name'] = sys.argv[1]
    return arguments

def main(arguments):
    name = arguments['person-name']
    print(f'Hi there, {name}!')


arguments = parse_command_line()
if 'person-name' not in arguments:
    print(usage_statement())
else:
    main(arguments)


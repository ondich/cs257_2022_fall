'''
    csv-sample.py
    Jeff Ondich, 27 September 2022

    Reading from and writing to comma-separated value files
    using the csv module.
'''

import sys
import csv

def get_all_authors(csv_file_name):
    ''' Returns a set of (surname, given name) ordered pairs, only one
        per author regardless how many books have the same author. '''
    authors = set()
    with open(csv_file_name) as input_file:
        reader = csv.reader(input_file)
        for row in reader:
            assert len(row) == 4
            given_name = row[2]
            surname = row[3]
            authors.add((surname, given_name))
    return authors

def write_authors(csv_file_name, authors):
    ''' Writes the authors, sorted by name, to the specified file as a two-column CSV file.
        Assumes authors is a list or set of ordered pairs (surname, given name). '''
    with open(csv_file_name, 'w') as output_file:
        writer = csv.writer(output_file)
        for surname, given_name in sorted(authors):
            row = [surname, given_name]
            writer.writerow(row)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} books-input-file authors-output-file')
        exit()

    # Get the authors out of the books CSV file
    books_input_file = sys.argv[1]
    authors = get_all_authors(books_input_file)

    # Write just the authors to a separate CSV file
    authors_output_file = sys.argv[2]
    write_authors(authors_output_file, authors)


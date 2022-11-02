Setting up the books/authors database
CS257 Software Design
Fall 2020
Jeff Ondich

How to set up my books/authors data so you can run my sample web application.

1. Creating the database.

    $ psql -U YOUR_PSQL_USER_NAME postgres
    postgres=# CREATE DATABASE books;

or just

    $ createdb books

(where $ is a Unix prompt, and postgres=# is a psql prompt).

2. Populating the database.

    $ psql -U YOUR_PSQL_USER_NAME books < books.sql


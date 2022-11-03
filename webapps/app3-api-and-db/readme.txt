Running the books/authors web application
CS257 Software Design
Winter 2021
Jeff Ondich

0. Read all the code!

This sample contains simple examples of all or nearly all of the techniques you will need to complete your web application. Read the code, collect questions, and ask them.

To run this example on your own machine

- Set up the database of books and authors. See app3-api-and-db/data/readme.txt for instructions.

- Pick your port. I'll use 5000 in my examples

- Change config.py to use whatever database, user, and password works on your machine.

- Launch the web application & API

    python3 books_webapp.py 127.0.0.1 5000

- Try it out. Direct your browser to:

    http://127.0.0.1:5000/

Assuming all goes well, you'll be able to click on the "Get Authors" button and get the list of authors.


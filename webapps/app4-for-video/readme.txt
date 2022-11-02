Running the books/authors web application
CS257 Software Design
Winter 2021
Jeff Ondich

0. What's going on in this app?

This is a sample that I used for a few terms of CS257 to demonstrate how to combine Flask, Javascript, and PostgreSQL in one package. And in particular, I made a video based on this app to illustrate various techniques.

In the meantime, I have developed a somewhat simpler (and, I hope, more helpful) sample for the same purpose, which is found in this repository in webapps/app3-api-and-db/. But I haven't remade the video.

So I recommend that you test out and study app3-api-and-db as a better model for your own project, but you'll probably want this app4-for-video application when you're watching the video.


1. Read all the code!

This sample contains simple examples of all or nearly all of the techniques you will need to complete your web application. Read the code, collect questions, and ask them.


2. Running this example on your own machine

(a) Set up the database of books and authors. See webapps/app4-for-video/data/readme.txt for instructions.

(b) Pick your port. I'll use 5000 in my examples

(c) Change config.py to use whatever database, user, and password works on your machine.

(d) Launch the web application & API

    python3 books_webapp.py localhost 5000

(e) Try it out. Direct your browser to:

    http://localhost:5000/

Assuming all goes well, you'll be able to click on the "Get Authors" button and get the list of authors.



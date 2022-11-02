Flask web app samples
Jeff Ondich
6 November 2021

This folder contains a collection of sample Flask apps.

app1-just-html - This one shows a Flask app with two HTML pages and not much else. No Javascript, no API, no database.

app2-with-api - This is a Flask app with a front-end in app.py (i.e. routes that yield HTML pages) and a back-end in api.py (i.e. routes that yield JSON). Two connect the front-end to the back-end, we have Javascript that demonstrates how to issue API calls and use the results to modify what the user sees.

app3-api-and-db - This sample extends the ideas in app2-with-api to access books & authors data stored in a postgres database.

app4-for-video - This is a sample that I used for a few terms of CS257 to demonstrate how to combine Flask, Javascript, and PostgreSQL in one package. And in particular, I made a video based on this app to illustrate various techniques. In the meantime, I developed the simpler (and, I hope, more helpful) sample app3-api-and-db for the same purpose. But since I haven't remade the video, app4-for-video is here so you can consult it while watching the video.


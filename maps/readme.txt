Maps samples using the Datamaps library
Jeff Ondich, 11 November 2020

Datamaps is Copyright (c) 2012 Mark DiMarco
https://github.com/markmarkoh/datamaps

BACKGROUND

There are many map-drawing libraries for Javascript. I've spent some time hunting for them, and I have found this one, Datamaps by Mark DiMarco, to be the easiest to use for drawing interactive US and World maps.

If you clone the Datamaps GitHub repository, you'll find lots of documentation and many examples. However, just loading the samples into a browser doesn't work. You have to make sure all the <link> and <script> tags, among other things, are pointing to the right places, and those places aren't where the files live in the repo.

So I have stripped out the bare essentials from Datamaps, created a US sample and a very similar World sample, and saved it all here. If you want fancier features than I have demonstrated here, you should go to GitHub link above and start reading.


USING THESE SAMPLES

- Pick either the US or World map sample to look at. They are nearly identical, but you might as well study the one that's relevant to your project. Below, wherever you see "usa", you can substitute "world" if you're using the world map.
- Open map-sample-usa.html in your browser. Try hovering over various states or countries. Try clicking on a state or country (and pay attention when you do to the upper-right of the page).
- Study the map-sample-usa.html, css/map-sample-usa.css, and js/map-sample-usa.js files.
- To incorporate these samples in your project, you'll need to
    * include the three <script> tags from the top of map-sample-usa.html in your HTML
    * include the js/datamaps.usa.min.js file in your project (e.g. your static/ folder in a Flask app)
    * incorporate the pieces of js/maps-sample-usa.js into your Javascript
    * of course, don't just use the extraStateInfo variable at the top of js/map-sample-usa.js; you'll
        need to assemble your relevant dictionaries before the "new Datamap" line gets executed


FEATURES OF THESE SAMPLES

Here are the features I have demonstrated.

- Creating a map, and adjusting the default colors
- Doing something interesting when the user clicks on a state/country
- Showing something interesting when the user hovers over a state/country
- Coloring selected states/countries

There are tons of things I could imagine doing that aren't on this list, but this is a start. Check out the info at https://github.com/markmarkoh/datamaps for lots more detail.


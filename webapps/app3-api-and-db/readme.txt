Running the books/authors web application
CS257 Software Design
Winter 2021
Jeff Ondich

0. Read all the code!

This sample contains simple examples of all or nearly all of the techniques you will need to complete your web application. Read the code, collect questions, and ask them.


1. Running this example on your own machine

(a) Set up the database of books and authors. See app3-api-and-db/data/readme.txt for instructions.

(b) Pick your port. I'll use 5000 in my examples

(c) Change config.py to use whatever database, user, and password works on your machine.

(d) Launch the web application & API

    python3 books_webapp.py localhost 5000

(e) Try it out. Direct your browser to:

    http://localhost:5000/

Assuming all goes well, you'll be able to click on the "Get Authors" button and get the list of authors.


2. [COMPLETELY, TOTALLY OPTIONAL] Running this example on perlman.mathcs.carleton.edu

I am providing these instructions in case you want to deploy your website so that other people can view it. I am not requiring you to do so, nor will I even to check to see whether you have done so. Furthermore, note that perlman is not accessible from outside the Carleton network, so anybody off campus who wants to view your website will need to be connected to Carleton's VPN first.

With those caveats in mind, here's how you can set up the books webapp on perlman. Modify these instructions as appropriate to launch your own webapp instead.

2.1 Launch your web app

(a) Connect to the Carleton network. Either do your work from on campus, or use Carleton's VPN to connect to the campus network. VPN instructions are here: https://apps.carleton.edu/campus/its/services/accounts/offcampus/

(b) Login to perlman.mathcs.carleton.edu

    ssh YOURUSERNAME@perlman.mathcs.carleton.edu

The first time, it will bug you like so:

    The authenticity of host 'perlman.mathcs.carleton.edu (137.22.4.17)' can't be established.
    ECDSA key fingerprint is SHA256:SNNPkZGLd/E9fOOeYOVsq6zkaQ26aCRv128fXSrK/B0.
    Are you sure you want to continue connecting (yes/no/[fingerprint])?

If the fingerprint listed is exactly as shown here, then type yes and hit Enter. Otherwise, type no and then let Mike Tie (mtie) and me know immediately, preferably with a screenshot.

(c) Go to your perlman web directory

    cd /Accounts/courses/cs257/jondich/web-w2021/YOURUSERNAME

(d) Grab a clone of this repository and go to the books-webapp directory

    git clone https://github.com/ondich/cs257_2021_winter
    cd cs257_2021_winter/books-webapp

(e) Obtain the port numbers that are available for your use. I will post them on Slack. I'll call your port number YOURPORT below.

(f) Set up the database of books and authors. See books-webapp/data/readme.txt for instructions.

(g) Change config.py to use your perlman user name (i.e. your Carleton user name) for both user and database, and the empty string for password.

    user='YOURUSERNAME'
    database='YOURUSERNAME'
    password=''

(h) Create and launch a "screen" session. For your purposes, the Unix command screen will enable you to run a process in the background (specifically, your web server) even when you are logged out. To learn more about screen, "man screen" will get you started.

    screen -S YOURUSERNAME_books

I'm suggesting YOURUSERNAME_books for your screen session's name for clarity, but you can name it anything you like.

(i) Launch the web application & API. (Note that you need to use perlman.mathcs.carleton.edu as the host, NOT localhost.)

    python3 books_webapp.py perlman.mathcs.carleton.edu YOURPORT

(j) Try it out. Direct your browser to:

    http://perlman.mathcs.carleton.edu:YOURPORT/

Assuming all goes well, you'll be able to click on the "Get Authors" button and get the list of authors.

(k) "Detach" from the screen session.

    Ctrl-A followed by d

(l) Logout, if you wish.

    exit


2.2 Shut your web app down

If you want to shut it down or just add features and relaunch, here's how.

(a) Connect to the Carleton network and login to perlman, as described in 2.1 above.

(b) Get a list of your active screen sessions.

    screen -ls

When I did this while writing these instructions, the resulting output looked like this:

    There is a screen on:
        11943.jondich_books	(Detached)
    1 Socket in /var/run/screen/S-jondich.

(c) "Attach" to your screen session. That is, you want to go back into the screen session so you can, for example, terminate your running server. You'll use the screen ID that appeared when you did "screen -ls", of course. For me, the attaching command was:

    screen -r jondich_books
or
    screen -r 11943
or
    screen -r 11943.jondich_books

(all three of these work).  

You should now see the recent logs from your web server, which has been running in the screen all this time.

(d) Want to terminate your server?

    Ctrl-C

(e) Want to keep your screen alive? Detach from it.

    Ctrl-A followed by d

Want to be done with your screen for good?

    exit


That's all, folks!

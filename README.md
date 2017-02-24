# Savant

### Savant is an encompassing social presence designer, built to promote online growth through predictive analytics and media consolidation.

[![Build Status](https://travis-ci.org/nicl7004/twitterToy.svg?branch=master)](https://travis-ci.org/nicl7004/twitterToy)

Website: http://nicl7004.github.io/twitterToy/

## Installation:

1. Go to https://dev.twitter.com/ and set up a developer account, you are going to need an Application Name, a Consumer Key, a Consumer Secret, an Access Token, and an Access Secret.  Next input all of this information into /modules/config.py for later use.

2. Run database/create_db.py, this will create a sqlite3 database to write users into temporarily for later analysis.  This database is intended to serve as a cache, and allow us fewer API calls for better results.

3. Install twitter library using `sudo pip3 install twitter`.

4. You're good to go! That should be everything necessary to run the current modules.


## Usage:

### /database:

This is where the database (graph.db) and all database helper scripts live.  The database is sqlite3, and is intended to save API calls and increase the accuracy of metrics by providing more data.

### /modules

These are the different metrics currently available with twitterToy. So far there is:

`config.py` - Contains all necessary tokens and secrets gathered from https://dev.twitter.com/.

`findFriends.py` - Returns a list of the users friends, can search based on username, full-name, or description (otherwise known as biography).  The username, full-name, or description currently have to be an exact match for this program be successful.

`followers-tweets-scatter.py` - Prints a scatter plot of Followers vs Tweets with data from the database.  This is helpful in identifying a correlation between how often an account tweets and the number of accounts following that account.
Here is a basic example with upper-bounds of 50,000 for number of tweets and number of followers.
![alt text](http://i.imgur.com/UHfsPpu.png)

`gather_data.py` - Currently writes to data table in graph.db.  Uses the api call to write unique data for each user. Updates following fields: screen_name text, full_name text, description text, account_created text, number_favorites int, number_followers int, number_following int, id int, profile_image text, number_tweets int, protected int, location text,lang text, time_zone text, withheld_in_countries text.  withheld_in_countries is filled in with a temporary value currently as many users do not have this element attached to their username. Here is an example of gather_data running in the terminal: ![alt text](http://i.imgur.com/dxCyjhC.png)

`GUI.py` - Work in progress, in the future hoping to create a GUI for users to search their personal friends and view their personal analytics.

`network.py` - Work in progress, want to create a networkx graph showing connections between users, test theory of 6 degrees of separation.
Here is example visualization created with networkx and matplotlib: ![alt text](http://i.imgur.com/4v8M9B7.png)

### /todo:

1. Complete database migration from sqlite3 to postgre and use sqlalchemy
2. Transfer current modules to new views in flask
3. Fix current user single auth, make sure user input is salted
4. Move unit tests to flask app
5. Set up baby regression testing - travis-ci
6. Integrate two factor authorization with Twilio
7. Host on Heroku or AWS
7. Get HTTPS cert from Let's Encrypt
8. Create basic "Predictive Analytics" - Feature
9. Integrate shopify API for commerce handling
10. Get a sick job @ twitter lol

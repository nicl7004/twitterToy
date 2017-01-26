#Nicholas Clement
#DB helper scrpit

import os
import sys
sys.path.append('../..') #set path to recognize new twitterToy package
sys.path.insert(0, os.path.abspath('..'))
import sqlite3
import twitterToy.modules.config as config
import twitter
import time


# Check if the specified user is in the 'data' table in graph.db
def existsData(username):

    conn = sqlite3.connect("../database/graph.db")
    c = conn.cursor()
    c.execute("SELECT * FROM data WHERE screen_name =?", (username,))
    y = c.fetchall()
    c.close()
    if y:
        return True
    else:
        return False

# Check if the specified user is in the 'graph' table in graph.db
def existsNode(username):

    conn = sqlite3.connect('../database/graph.db')
    c = conn.cursor()
    c.execute("SELECT * FROM graph WHERE nodes =?", (username,))
    y = c.fetchall()
    c.close()
    if y:
        return True
    else:
        return False

# Check if the specified edge is in the 'graph' table in graph.db
def existsEdge(userone):

    conn = sqlite3.connect('../database/graph.db')
    c = conn.cursor()
    c.execute("SELECT * FROM graph WHERE nodes =?", (userone,))
    y = c.fetchall()
    c.close()
    if y:
        return True
    else:
        return False

# Adds edges to our graph
def addEdgeNode(userone, usertwo):

    ##/Users/nicholas/Desktop/pers-proj/twitterToy -> where test originates from

    ##/ Users / nicholas / Desktop / pers - proj / twitterToy /modules-> where functionality originates from

    print(sys.path)
    print("\n\n\n", os.getcwd(), "\n\n\n")

    if "modules" not in os.getcwd(): ##for the case of running from the test directory
        dbname = str(os.getcwd())
        dbname += "/database/graph.db"

        conn = sqlite3.connect(dbname)

    else:
        conn = sqlite3.connect('../database/graph.db') ##for the case of running from the modules directory

    c = conn.cursor()
    params = (userone, usertwo)
    c.execute("INSERT INTO graph VALUES(?,?)", params)
    conn.commit()
    conn.close()

# Gather all edges from the graph table for creation of networkx graph
def getEdge():

    conn = sqlite3.connect('../database/graph.db')
    c = conn.cursor()
    y = c.execute("SELECT * FROM graph")
    return(y)
    conn.close()

# Given a username gather information on all the users friends and write to our data table
def gatherUsersFriendsData(username):

    api = twitter.Api(consumer_key=config.consumerKey,
                      consumer_secret=config.consumerSecret,
                      access_token_key=config.accessToken,
                      access_token_secret=config.accessSecret,
                      sleep_on_rate_limit=True
                      )

    myFriends = api.GetFriends(screen_name = username)
    conn = sqlite3.connect('../database/graph.db')

    print("API Success\n")

    for each in myFriends:

        c = conn.cursor()
        params = (each.screen_name, each.name, each.description, each.created_at,
                each.favourites_count, each.followers_count, each.friends_count, each.id,
                each.profile_image_url, each.statuses_count, each.protected, each.location,
                each.lang, each.time_zone, "tmp")
        #Check if user already exists
        if existsData(each.screen_name):
            continue

        else:
            c.execute("INSERT INTO data VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", params)

    print("*****Wrote", len(myFriends),"users into database.*****")
    conn.commit()
    conn.close()

#return a random username from the database
def randomUser():
    conn = sqlite3.connect('../database/graph.db')
    c = conn.cursor()
    c.execute("SELECT screen_name, protected FROM data WHERE protected = 0 ORDER BY RANDOM() limit 1")
    for each in c: return (each[0], each[1])

#given a username gather the friend network of the user
def gatherUsersNetwork(username):

    listUsers = []
    if twitterToy.database.databaseHelper.existsEdge(username):
        print("User network already exists in database\n")
        return(-1)

    api = twitter.Api(consumer_key=twitterToy.modules.config.consumerKey,
                      consumer_secret=twitterToy.modules.config.consumerSecret,
                      access_token_key=twitterToy.modules.config.accessToken,
                      access_token_secret=twitterToy.modules.config.accessSecret,
                      sleep_on_rate_limit=True)
    friends = api.GetFriends(username)
    print("API was called")

    for each in friends:
        print(each)
        twitterToy.database.databaseHelper.addEdgeNode(username, each.screen_name)
        listUsers.append(each.screen_name)
    return listUsers

def main():
    y =0
    print(existsData('nickc873'))
    print(existsNode('test node'))
    print(existsEdge('test','edge'))
    print(randomUser())
    addEdgeNode("userone", "usertwo")

if __name__ == '__main__':
    main()

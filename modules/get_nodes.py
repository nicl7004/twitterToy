from urllib.request import Request, urlopen, URLError
import twitter
import time
import config
import oauth2
import sqlite3

import os
import sys
sys.path.append('../..') #set path to recognize new twitterToy package
import twitterToy.database.databaseHelper

batch = []

def userFriends(username):
    listUsers = []
    api = twitter.Api(consumer_key=config.consumerKey,
                      consumer_secret=config.consumerSecret,
                      access_token_key=config.accessToken,
                      access_token_secret=config.accessSecret)
    friends = api.GetFriends(username)

    for each in friends:
        twitterToy.database.databaseHelper.addEdgeNode(username, each.screen_name)
        listUsers.append(each.screen_name)




if __name__ == '__main__':

    name = input("Please type the username of the person to add to the graph.\n")

    batch = userFriends(name)

    orig = batch

    workfile = open('workfile.txt','w')
    workfile.write("\n\n***********************************************\n", name, "\n***********************************************\n")

    for each in batch:
        workfile.write(each,"\n")




    main()

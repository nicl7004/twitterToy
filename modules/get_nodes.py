import twitter

import os
import sys
sys.path.append('../..') #set path to recognize new twitterToy package
import twitterToy.database.databaseHelper


def userFriends(username):
    listUsers = []
    print("API was called")
    api = twitter.Api(consumer_key=config.consumerKey,
                      consumer_secret=config.consumerSecret,
                      access_token_key=config.accessToken,
                      access_token_secret=config.accessSecret)
    friends = api.GetFriends(username)

    for each in friends:
        twitterToy.database.databaseHelper.addEdgeNode(username, each.screen_name)
        listUsers.append(each.screen_name)
    return listUsers



if __name__ == '__main__':

    name = input("Please type the username of the person to add to the graph.\n")

    #checks if the users network has already been added to the database
    if twitterToy.database.databaseHelper.existsEdge(name):
        print("User network already exists in database\n")
    else:
        batch = userFriends(name)
        print(batch)

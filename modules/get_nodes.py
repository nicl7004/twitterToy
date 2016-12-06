import twitter

import os
import sys
sys.path.append('../..') #set path to recognize new twitterToy package
import twitterToy.database.databaseHelper as db_helper
import twitterToy.modules.config

def userFriends(username):
    listUsers = []
    if twitterToy.database.databaseHelper.existsEdge(username):
        print("User network already exists in database\n")
        return(-1)

    else:
        api = twitter.Api(consumer_key=twitterToy.modules.config.consumerKey,
                          consumer_secret=twitterToy.modules.config.consumerSecret,
                          access_token_key=twitterToy.modules.config.accessToken,
                          access_token_secret=twitterToy.modules.config.accessSecret,
                          sleep_on_rate_limit=True)
        friends = api.GetFriends(username)
        print("API was called")

        for each in friends:
            db_helper.addEdgeNode(username, each.screen_name)
            listUsers.append(each.screen_name)
        return listUsers

def main():
    name = input("Please type the username of the person to add to the graph.\n")

    #checks if the users network has already been added to the database
    batch = userFriends(name)
    print(batch)

if __name__ == '__main__':
    main()

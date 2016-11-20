import os
import sys
sys.path.append('../..') #set path to recognize new twitterToy package
import twitterToy.database.databaseHelper

from urllib.request import Request, urlopen, URLError

import twitter
import networkx as nx
import time
import config
import oauth2


api = twitter.Api(consumer_key=config.consumerKey,
                  consumer_secret=config.consumerSecret,
                  access_token_key=config.accessToken,
                  access_token_secret=config.accessSecret)


def userFriends(username):
    return api.GetFriends()


if __name__ == '__main__':

    # y = nx.Graph()

    for each in userFriends():
        # y.add_edge("nickc873", each.screen_name)
        twitterToy.database.databaseHelper.addEdgeNode("nickc873", each.screen_name)

    for each in y.nodes():
        x = api.GetFriends(screen_name =each)

        for friends in x:
            y.add_edge(each, friends.screen_name)
            print(y.nodes(), len(y.nodes()))

        input("Press Enter to continue...")


    print(y.nodes())

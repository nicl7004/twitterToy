
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


def userFriends():

    return api.GetFriends()


if __name__ == '__main__':
    y = nx.Graph()

    for each in userFriends():
        y.add_edge("nickc873", each.screen_name)
    for each in y.nodes():
        x = api.GetFriends(screen_name =each)

        for friends in x:
            y.add_edge(each, friends.screen_name)
            print(y.nodes(), len(y.nodes()))

        input("Press Enter to continue...")


    print(y.nodes())

# In process of moving all analyitics into single module


import os
import sys
sys.path.append('../..') #set path to recognize new twitterToy package
import twitter
import twitterToy.database.databaseHelper as db_helper
import networkx as nx
import matplotlib.pyplot as plt
import config

'''class for creating network from database
includes some visualizations'''
class network(object):

    def __init__(self): #init our class by creating the graph
        self.graph = nx.Graph()
        [self.graph.add_edge(each[0],each[1]) for each in db_helper.getEdge()]

    def draw(self): #visulaize network
        nx.draw_networkx(self.graph, pos=None, arrows=True, with_labels=True, font_size=8, width=0.05)
        plt.show()

    def networkSize(self): #show size of network
        return self.graph.size

''' Maybe want to move these classes into separate modules. Usually only want a single class per module '''
class user(object):

    def __init__(self):

        self.api = twitter.Api(consumer_key=config.consumerKey,
                          consumer_secret=config.consumerSecret,
                          access_token_key=config.accessToken,
                          access_token_secret=config.accessSecret
                          )

    def searchScreenName(self,username):

        try:
            for each in self.api.GetFriends(screen_name=username):
                db_helper.addEdgeNode(username, each.screen_name)
                print(each.screen_name)

        except twitter.error:
            print("Rate limit exceeded")


    def searchFullname(self,fullname):
        try:
            for each in self.api.GetFriends(name=fullname):
                db_helper.addEdgeNode(username, each.screen_name)
                print(each.screen_name)

        except twitter.error:
            print("Rate limit exceeded")


    def searchBio(self,bio):
        try:
            for each in self.api.GetFriends(description=description):
                db_helper.addEdgeNode(username, each.screen_name)
                print(each.screen_name)

        except twitter.error:
            print("Rate limit exceeded")


def main():
    y = user()
    y.searchScreenName("nickc873")

    x = network() #instance of network class
    x.draw()
    x.networkSize

if __name__ == '__main__':
    main()

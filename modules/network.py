import os
import sys
sys.path.append('../..') #set path to recognize new twitterToy package
import twitterToy.database.databaseHelper

import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':

    network = nx.Graph()

    [network.add_edge(each[0],each[1]) for each in twitterToy.database.databaseHelper.getEdge()]

    print(network.nodes())
    print(network.edges())

    nx.draw_networkx(network, pos=None, arrows=True, with_labels=True)
    plt.show()

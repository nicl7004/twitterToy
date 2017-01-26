import networkx as nx
import sys
import matplotlib.pyplot as plt
sys.path.append('../..') #set path to recognize new twitterToy package
import twitterToy.database.databaseHelper as db_helper
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
        return self.graph.size()

def main():
    x = network() #instance of network class
    print(x.networkSize())
    x.draw()


if __name__ == '__main__':
    main()

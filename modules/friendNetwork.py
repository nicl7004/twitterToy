'''given a file with a list of names add each name's network to the database and then delete it from
that given file.

This is intened to keep track of a longer list of names that will overuse the API but keep our posistion
in what names have been added and what names have not been added.'''

import os
import sys
sys.path.append('../..') #set path to recognize new twitterToy package
import twitterToy.database.databaseHelper
import twitterToy.modules.get_nodes

import twitter

#start by getting each line of file in this function
def getContents(filename):
    f = open(filename,"r")
    lines = f.readlines()
    return(lines)
    f.close()


if __name__ == '__main__':

    lines = getContents("friends.txt")
    print(lines)
    #reopen file and prepare to overwrite users we run API search on
    f = open("friends.txt","w")
    for each in lines:
        print (each)
        twitterToy.modules.get_nodes.userFriends(each)
        f.write("\n")

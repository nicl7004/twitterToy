#call API and write to database
#use the gather friends function on a random user in the database
from urllib.request import Request, urlopen, URLError
import twitter
import time
import random
import config
import oauth2
import sqlite3

import os
import sys
sys.path.append('../..') #set path to recognize new twitterToy package
import twitterToy.database.databaseHelper



if __name__ == "__main__":






    while True:
        protected = 0
        x = random.randint(60,65)

        while protected == 0:
            z = twitterToy.database.databaseHelper.randomUser()
            #check to see if we can access users friends depending on privacy settings
            if z[1] == 0:
                try:
                    print("Calling API on user:", z[0],"with privacy ==", z[1])
                    twitterToy.database.databaseHelper.gatherUsersFriendsData(z[0])
                    protected +=1

                except twitter.error.TwitterError:
                    print("Error occured")
                    break

        print("waiting", x, "seconds")
        print("*******************************\n\n")

        for i in range(x, 0, -1):
            print(i, end='\r')
            time.sleep(1)

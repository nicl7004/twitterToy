# In process of moving all analyitics into single module

import os
import sys
import twitter
if sys.version_info[0] < 3: #for python 2.7 and under
    (sys.path.append(str(os.path.abspath('..')) + "/twitterToy/"))
    from database import databaseHelper as db_helper
    from modules import config as config

else:                       #for python 3 and up
    sys.path.insert(0, os.path.abspath('..'))
    sys.path.append('../..') #set path to recognize new twitterToy package
    import twitterToy.database.databaseHelper as db_helper
    import twitterToy.modules.config as config


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


if __name__ == '__main__':
    main()

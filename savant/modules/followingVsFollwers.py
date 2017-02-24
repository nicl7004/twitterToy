#Checks the specified users followers vs who they are following, tell them who is not following back
# Upper limit is currently 3000 followers

import os
import sys
import twitter

try: #for python 2.7 and under
    (sys.path.append(str(os.path.abspath('..')) + "/twitterToy/"))
    from modules import config as config

except ImportError:                       #for python 3 and up
    sys.path.insert(0, os.path.abspath('..'))
    sys.path.append('../..') #set path to recognize new twitterToy package
    import twitterToy.modules.config as config


class followingVsFollwers(object):

    def __init__(self):

        self.api = twitter.Api(consumer_key=config.consumerKey,
                          consumer_secret=config.consumerSecret,
                          access_token_key=config.accessToken,
                          access_token_secret=config.accessSecret
                          )

    def following(self, userName):
        x = []
        try:
            [(x.append(each.screen_name))for each in self.api.GetFriends(screen_name=userName, total_count=3000)]
        except twitter.error.TwitterError:
            print("Error occured.", twitter.error.TwitterError)

        return x

    def followers(self, userName):
        x = []
        try:
            # for each in self.api.GetFollowers(screen_name=userName):
            #     print(each)
            [(x.append(each.screen_name)) for each in self.api.GetFollowers(screen_name=userName, total_count=3000)]
        except twitter.error.TwitterError:
            print("Error occured.", twitter.error.TwitterError)

        return x

    def compare(self, userName):

        following = self.following(userName)
        followers = self.followers(userName)

        difference = len(following) - len(followers)

        notFollowing = []

        for each in following:
            if each in followers:
                continue
            else:
                notFollowing.append(each)

        return (difference, notFollowing)
def main():

    username = input("Whats the username you want to compare followers vs following on?")
    track = followingVsFollwers()
    result = track.compare(username)

    print("\n\n\nYou have", result[0], "less followers than people you follow.\n\n", "People you follow who don't follow you are:", result[1], "\n\n\n")

if __name__ == '__main__':
    main()

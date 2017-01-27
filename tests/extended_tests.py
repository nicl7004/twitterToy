# set path to recognize new twitterToy package
# sys.path.append('/modules')
import sys
import os
import unittest

if sys.version_info[0] < 3:  # for python 2.7 and under
    (sys.path.append(str(os.path.abspath('..')) + "/twitterToy/"))
    from modules import user, followingVsFollwers, followers_tweets_scatter
    from database import databaseHelper

else:  # for python 3 and up
    sys.path.insert(0, os.path.abspath('..'))
    sys.path.append('../..')
    from twitterToy.modules import user, followingVsFollwers, followers_tweets_scatter
    from twitterToy.database import databaseHelper


class SimplisticTest(unittest.TestCase):
    # modules tests
    def testSearchScreenName(self):
        y = user.user()
        y.searchScreenName("nickc873")

    def testFollowersTweetsScatter(self):
        followers_tweets_scatter.followers_tweets_scatter()

    def testfollowingVsFollwers(self):
        y = followingVsFollwers.followingVsFollwers()
        y.compare("nickc873")

    # database tests
    def testEmailList(self):
        databaseHelper.getEmailList()

    def testNetwork(self):
        x = network.network()
        x.draw()
        x.networkSize()


if __name__ == '__main__':
    unittest.main()
    x = 0



 #set path to recognize new twitterToy package
# sys.path.append('/modules')
import sys
import os
import unittest

# if sys.version_info[0] < 3: #for python 2.7 and under
try:
    (sys.path.append(str(os.path.abspath('..')) + "/twitterToy/"))
    from modules import user, followingVsFollwers, followers_tweets_scatter, globalTrends
    from database import databaseHelper

except ImportError:                       #for python 3 and up
    sys.path.insert(0, os.path.abspath('..'))
    sys.path.append('../..')
    from twitterToy.modules import user, followingVsFollwers, followers_tweets_scatter, globalTrends
    from twitterToy.database import databaseHelper

class SimplisticTest(unittest.TestCase):
    #modules tests
    def testSearchScreenName(self):
        y = user.user()
        y.searchScreenName("nickc873")

    def testFollowersTweetsScatter(self):
        followers_tweets_scatter.followers_tweets_scatter()

    def testfollowingVsFollwers(self):
        y = followingVsFollwers.followingVsFollwers()
        y.compare("nickc873")

    #database tests
    def testEmailList(self):
        databaseHelper.getEmailList()

    def testTrend(self):
        trend = globalTrends.trends()
        trend.getGlobalTrends()

    def testTrendWash(self):
        x = globalTrends.trends()
        unwashed = x.getGlobalTrends()
        washed = x.washTrend(unwashed)

    def testTrendEmail(self):
        x = globalTrends.trends()
        unwashed = x.getGlobalTrends()
        washed = x.washTrend(unwashed)
        x.sendEmail("nicholas.clement@colorado.edu", "Twitter Trending Update", washed)







if __name__ == '__main__':
    unittest.main()
    x = 0

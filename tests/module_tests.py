 #set path to recognize new twitterToy package
# sys.path.append('/modules')
import sys
import os
import unittest
sys.path.append('../..')
sys.path.insert(0, os.path.abspath('..'))
from twitterToy.modules import user
from twitterToy.modules import followers_tweets_scatter
# from twittertoy.modules import user as user
# import modules.user as user

class SimplisticTest(unittest.TestCase):

    def testSearchScreenName(self):
        y = user.user()
        y.searchScreenName("nickc873")

    def testFollowersTweetsScatter(self):
        followers_tweets_scatter.followers_tweets_scatter()




if __name__ == '__main__':
    unittest.main()
    x = 0
    print(sys.path)


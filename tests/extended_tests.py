 #set path to recognize new twitterToy package
# sys.path.append('/modules')
import sys
import os
import unittest


if sys.version_info[0] < 3: #for python 2.7 and under
    (sys.path.append(str(os.path.abspath('..')) + "/twitterToy/"))
    from modules import user
    from modules import followers_tweets_scatter
    from modules import network

else:                       #for python 3 and up
    sys.path.insert(0, os.path.abspath('..'))
    sys.path.append('../..')
    from twitterToy.modules import user
    from twitterToy.modules import followers_tweets_scatter
    from twitterToy.modules import network


class SimplisticTest(unittest.TestCase):

    def testSearchScreenName(self):
        y = user.user()
        y.searchScreenName("nickc873")

    def testFollowersTweetsScatter(self):
        followers_tweets_scatter.followers_tweets_scatter()

    def testNetwork(self):
        x = network.network()
        x.draw()
        x.networkSize()





if __name__ == '__main__':
    unittest.main()
    x = 0



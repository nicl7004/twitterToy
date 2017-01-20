
import unittest

from modules import user
# import modules.user as user

class SimplisticTest(unittest.TestCase):

    def testSearchScreenName(self, screenName):
        y = user.user()
        y.searchScreenName("nickc873")


if __name__ == '__main__':
    unittest.main()

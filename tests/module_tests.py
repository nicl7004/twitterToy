
import sys
sys.path.append('../..') #set path to recognize new twitterToy package
import twitterToy.modules.user as user
def main():
    y = user.user()
    y.searchScreenName("nickc873")


if __name__ == '__main__':
    main()

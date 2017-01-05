
import sys
import os
# sys.path.append(str(os.path.dirname(os.path.abspath("module_tests.py"))).replace("/tests",""))
# print(str(os.path.dirname(os.path.abspath("module_tests.py"))).replace("/tests",""),"\n\n")
# sys.path.append('~/twitterToy') #set path to recognize new twitterToy package
# sys.path.append("../..")
print (sys.path)
import twitterToy.modules.user as user

def main():
    y = user.user()
    y.searchScreenName("nickc873")


if __name__ == '__main__':
    main()

from urllib.request import Request, urlopen, URLError
import twitter
import time
import config
import oauth2



if __name__ == '__main__':

    api = twitter.Api(consumer_key=config.consumerKey,
                      consumer_secret=config.consumerSecret,
                      access_token_key=config.accessToken,
                      access_token_secret=config.accessSecret
                      )

    while True:
        choice = input("Type s if you would like to search on screen_name\nType n if you would like to search on full name\nType d if you would like to search on description\nType q if you would like to quit\n")

        if choice == 's' or choice == 'S':
            name = input('Enter screen name\n')
            try:
                [print(each.screen_name) for each in api.GetFriends(screen_name = name)]
            except twitter.error.TwitterError:
                print("Rate limit exceeded")
                break

        elif choice == 'n' or choice == 'N':
            name = input('Enter users full name\n')
            try:
                [print(each.screen_name) for each in api.GetFriends(name = name)]
            except twitter.error.TwitterError:
                print("Rate limit exceeded")
                break

        elif choice == 'd' or choice == 'D':
            description = input('Enter users full bio\n')
            try:
                [print(each.screen_name) for each in api.GetFriends(description = description)]
            except twitter.error.TwitterError:
                print("Rate limit exceeded")
                break

        elif choice == 'q' or choice == 'Q':
            break

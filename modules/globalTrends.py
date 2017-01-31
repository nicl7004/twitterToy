#Gathers the global trends and forwards them to users on the email list via email

import os
import sys
import twitter
import smtplib #to send email



try: #for python 2.7 and under
    (sys.path.append(str(os.path.abspath('..')) + "/twitterToy/"))
    from modules import config as config
    # from database import databaseHelper

except ImportError:                       #for python 3 and up
    sys.path.insert(0, os.path.abspath('..'))
    sys.path.append('../..') #set path to recognize new twitterToy package
    import twitterToy.modules.config as config
    # from twitterToy.database import databaseHelper


class trends(object):

    def __init__(self):
        self.api = twitter.Api(consumer_key=config.consumerKey,
                               consumer_secret=config.consumerSecret,
                               access_token_key=config.accessToken,
                               access_token_secret=config.accessSecret
                               )

    def getGlobalTrends(self):
        return(self.api.GetTrendsCurrent(exclude=None))

    def washTrend(self, trends): #fix this currently displays only top item
        gTrends = []
        [(gTrends.append(each.name)) for each in trends]

        x = ''
        y = ''

        # print(gTrends)
        washed = ''
        for each in gTrends:
            # for letter in each:
            #     if ord(letter) < 128:
            #         x += letter
            #     else:
            #         continue

            try:
                each.encode("ascii")
                washed += ' '
                washed += each
            except UnicodeEncodeError:
                continue

        print(washed)
        return washed



    def sendEmail(self, recip, subject, message):

        messageA = "From: twittertoyoffical@gmail.com"
        messageB = "To: " + recip
        messageC = "Subject: " + subject
        sender = 'twittertoyoffical@gmail.com'
        i = 0
        totalMessage = messageA + "\n" + messageB + "\n" + messageC + "\n\n" + message

        try:
            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.ehlo()
            session.starttls()
            session.ehlo()
            session.login(sender, 'abcdefg123456')
            session.sendmail(sender, recip, totalMessage)
            session.quit()

        except smtplib.SMTPException:
            print ("Error: unable to send email")
        i +=1
        print("Success, sent to", recip, i, "\n\n")


def main():

    x = trends()
    unwashed = x.getGlobalTrends()
    washed = x.washTrend(unwashed)
    # print(washed)
    x.sendEmail("nicholas.clement@colorado.edu", "Twitter Trending Update", washed)

if __name__ == '__main__':
    main()

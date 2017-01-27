#Gathers the global trends and forwards them to users on the email list via email

import os
import sys
import twitter
import smtplib #to send email



if sys.version_info[0] < 3: #for python 2.7 and under
    (sys.path.append(str(os.path.abspath('..')) + "/twitterToy/"))
    from modules import config as config
    from database import databaseHelper

else:                       #for python 3 and up
    sys.path.insert(0, os.path.abspath('..'))
    sys.path.append('../..') #set path to recognize new twitterToy package
    import twitterToy.modules.config as config
    from twitterToy.database import databaseHelper


class trends(object):

    def __init__(self):
        self.api = twitter.Api(consumer_key=config.consumerKey,
                               consumer_secret=config.consumerSecret,
                               access_token_key=config.accessToken,
                               access_token_secret=config.accessSecret
                               )

    def getGlobalTrends(self):
        return(self.api.GetTrendsCurrent(exclude=None))

def main():
    x = trends()
    gTrends = []
    listEmails = []
    recievers = []

    [(gTrends.append(each.name)) for each in x.getGlobalTrends()]
    for each in x.getGlobalTrends():
        try:
            x = str(each)
            x.encode('ascii', errors='strict')
            gTrends.append(x)
        except UnicodeEncodeError:
            continue


    emailsObject = databaseHelper.getEmailList()

    [(listEmails.append((next[1], next[2]))) for next in emailsObject]
    [(recievers.append(next[2])) for next in emailsObject]

    print(listEmails)
    print(gTrends)
    contents = str(",".join(gTrends)).replace(",", ", ")


    sender = 'nicholasclement21@gmail.com'

    for each in listEmails:
        messageA = "From: nicholasclement21@gmail.com\n"
        messageB = "To: " +str(each[0]) + "\n"
        messageC = "Subject: Current Trends\n"
        totalMessage = messageA + messageB + messageC + contents

        print(totalMessage)

        try:
            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.ehlo()
            session.starttls()
            session.ehlo()
            session.login(sender, '!1Laurel12')
            session.sendmail(sender, each[1], totalMessage)
            session.quit()

        except smtplib.SMTPException:
            print ("Error: unable to send email")



if __name__ == '__main__':
    main()
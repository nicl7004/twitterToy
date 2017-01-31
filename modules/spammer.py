import smtplib #to send email
import random
#abcdefg123456
#twittertoyoffical@gmail.com

class spammer(object):

    def sendEmail(recip, subject, message):

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
    message = ['I dreamt I was forced to eat a giant marshmallow. When I woke up, my pillow was gone', '''Doctor: "I'm sorry but you suffer from a terminal illness and have only 10 to live."
Patient: "What do you mean, 10? 10 what? Months? Weeks?!" Doctor: "Nine."''', '''Two Elephants meet a totally naked guy. After a while one elephant says to the other: “I really don’t get how he can feed himself with that thing!”''',
'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.']
    for each in range(1,100,1):
        x = random.randint(0, len(message)-1)
        spammer.sendEmail('michael.vienneau@colorado.edu', message[x], 'Good morning fam')
        # spammer.sendEmail('brennon.lee@colorado.edu', 'suh du', 'Good morning fam')
        print(each)
# michael.vienneau@colorado.edu
if __name__ == '__main__':
    main()

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
Patient: "What do you mean, 10? 10 what? Months? Weeks?!" Doctor: "Nine."''', '''Two Elephants meet a totally naked guy. After a while one elephant says to the other: I really don’t get how he can feed himself with that thing!''',
'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 'My wife and I were happy for twenty years. Then we met.', 'Feeling pretty proud of myself. The Sesame Street puzzle I bought said 3-5 years, but I finished it in 18 months.',
'A recent study has found that women who carry a little extra weight live longer than the men who mention it.', 'If i had a dollar for every girl that found me unattractive, they would eventually find me attractive.', 'Just read that 4,153,237 people got married last year, not to cause any trouble but shouldnt that be an even number?',
'Life is like toilet paper, youre either on a roll or taking shit from some asshole.', 'I find it ironic that the colors red, white, and blue stand for freedom until they are flashing behind you.',
'I want to die peacefully in my sleep, like my grandfather.. Not screaming and yelling like the passengers in his car.', 'When wearing a bikini, women reveal 90 % of their body... men are so polite they only look at the covered parts.','Im great at multitasking. I can waste time, be unproductive, and procrastinate all at once.',
'Politicians and diapers have one thing in common. They should both be changed regularly, and for the same reason.', 'When my boss asked me who is the stupid one, me or him? I told him everyone knows he doesnt hire stupid people.', 'People used to laugh at me when I would say "I want to be a comedian", well nobodys laughing now.',
'Alcohol is a perfect solvent: It dissolves marriages, families and careers.', 'Apparently I snore so loudly that it scares everyone in the car Im driving.']
    for each in range(1,100,1):
        x = random.randint(0, len(message)-1)
        print(message[x])
        try:
            message[x].encode("ascii")
        except UnicodeEncodeError:

            continue
        subject = 'Good morning fam, joke number ' + str(x)
        spammer.sendEmail('nicholas.clement@colorado.edu', subject, message[x])
        # spammer.sendEmail('brennon.lee@colorado.edu', 'suh du', 'Good morning fam')
        print('Email number:', each, "Subject:", subject)
# michael.vienneau@colorado.edu
if __name__ == '__main__':
    main()

#Nicholas Clement
#DB helper scrpit

import sqlite3
import config
import twitter
import time
import config
import oauth2
# Check if the specified user is in the 'data' table in graph.db
def existsData(username):
    conn = sqlite3.connect('graph.db')
    c = conn.cursor()
    c.execute("SELECT * FROM data WHERE screen_name =?", (username,))
    y = c.fetchall()
    c.close()
    if y:
        return True
    else:
        return False
# Check if the specified user is in the 'graph' table in graph.db
def existsNode(username):
    conn = sqlite3.connect('graph.db')
    c = conn.cursor()
    c.execute("SELECT * FROM graph WHERE nodes =?", (username,))
    y = c.fetchall()
    c.close()
    if y:
        return True
    else:
        return False
# Check if the specified edge is in the 'graph' table in graph.db
def existsEdge(userone, usertwo):
    query = userone+" " + usertwo
    conn = sqlite3.connect('graph.db')
    c = conn.cursor()
    c.execute("SELECT * FROM graph WHERE edges =?", (query,))
    y = c.fetchall()
    c.close()
    if y:
        return True
    else:
        return False
# Given a username gather information on all the users friends and write to our data table
def gatherUsersFriendsData(username):

    api = twitter.Api(consumer_key=config.consumerKey,
                      consumer_secret=config.consumerSecret,
                      access_token_key=config.accessToken,
                      access_token_secret=config.accessSecret,
                      sleep_on_rate_limit=True
                      )

    myFriends = api.GetFriends(screen_name = username)
    conn = sqlite3.connect('graph.db')

    print("API Success\n")

    for each in myFriends:

        c = conn.cursor()
        params = (each.screen_name, each.name, each.description, each.created_at,
                each.favourites_count, each.followers_count, each.friends_count, each.id,
                each.profile_image_url, each.statuses_count, each.protected, each.location,
                each.lang, each.time_zone, "tmp")
        #Check if user already exists
        if existsData(each.screen_name):
            continue

        else:
            c.execute("INSERT INTO data VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", params)

    print("*****Wrote", len(myFriends),"users into database.*****")
    conn.commit()
    conn.close()

#return a random username from the database
def randomUser():
    conn = sqlite3.connect('graph.db')
    c = conn.cursor()
    c.execute("SELECT screen_name, protected FROM data ORDER BY RANDOM() limit 1")
    for each in c: return (each[0], each[1])




def main():
    y =0
    print(existsData('nickc873'))
    print(existsNode('test node'))
    print(existsEdge('test','edge'))
    while y == 0:
        x = randomUser()
        if x[1] == 0:
            y +=1
            print(x)
        else:
            continue




if __name__ == '__main__':
    main()

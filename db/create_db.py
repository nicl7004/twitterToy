
from urllib.request import Request, urlopen, URLError
import twitter
import time
import sys
import twitterToy

import oauth2
import sqlite3


if __name__ == "__main__":

    conn = sqlite3.connect('graph.db')

    c = conn.cursor()

        Create table
    c.execute('''CREATE TABLE graph
                 (nodes text, edges text)''')
    c.execute('''CREATE TABLE data
                (screen_name text, full_name text, description text, account_created text, number_favorites int, number_followers int,
                number_following int, id int, profile_image text, number_tweets int )''')

    # Insert a row of data
    c.execute("INSERT INTO graph VALUES ('test node', 'test edge')")
    c.execute("INSERT INTO data VALUES('test', 'test','test','test', 1,1, 1, 1, 'test','test')")

    # Save (commit) the changes
    conn.commit()

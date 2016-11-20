
import os
import sys
sys.path.append('../..') #set path to recognize new twitterToy package

import sqlite3


if __name__ == "__main__":

    conn = sqlite3.connect('../graph.db')

    c = conn.cursor()


    c.execute('''CREATE TABLE graph
                 (nodes text, edges text)''')
    c.execute('''CREATE TABLE data
                (screen_name text, full_name text, description text, account_created text, number_favorites int, number_followers int,
                number_following int, id int, profile_image text, number_tweets int, protected int, location text,
                lang text, time_zone text, withheld_in_countries text)''')

    conn.commit()
    conn.close()

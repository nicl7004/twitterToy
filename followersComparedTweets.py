#Nicholas Clement
#Program to compare the number of followers a user has to the number of tweets they tweet.
import sqlite3
import matplotlib.pyplot as plt


if __name__ == '__main__':
    x = y = []

    conn = sqlite3.connect('graph.db')
    c = conn.cursor()

    data = c.execute("SELECT screen_name, number_tweets, number_followers FROM data where number_followers >= 1000")

    for intEach, each in enumerate(data):

        x.append([each[1], each[2]])

    print(x)
    plt.plot(*zip(*x), marker='o', color='r', ls='')
    plt.axis([0,5000,0,5000])
    plt.show()

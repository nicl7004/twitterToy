#Nicholas Clement
#Program to compare the number of followers a user has to the number of tweets they tweet.
import sqlite3
import matplotlib.pyplot as plt

def main():
    x = y = []

    conn = sqlite3.connect('../database/graph.db')
    c = conn.cursor()

    data = c.execute("SELECT screen_name, number_tweets, number_followers FROM data where number_followers >= 1000")

    [x.append([each[1], each[2]]) for each in data]

    plt.plot(*zip(*x), marker='o', color='r', ls='')
    plt.axis([0,50000,0,50000])
    plt.show()

if __name__ == '__main__':
    main()

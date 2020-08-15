import pickle
import json

def open_and_read_pickle(filename):
    with open(filename, 'rb') as file:
        try:
            while True:
                yield pickle.load(file)
        except EOFError:
            pass

def open_and_read_json(filename):
    with open(filename) as data_file:
        return json.load(data_file)

def open_and_read_txt(filename):
    with open(filename) as file:
        for line in file:
            pass

if __name__ == "__main__":
    # tweets = open_and_read_pickle('old_top_tweets_dat.dat')
    # total_tweets = 0
    # for date in tweets:
    #     try:
    #         print(date[0].date)
    #     except:
    #         pass
    #     print(len(date))
    #     total_tweets += len(date)
    #
    # print("Total tweets: ", total_tweets)
    # for tweet in date:
    #     if len(tweet.geo) == 0:
    #         pass
    #     else:
    #         print(tweet.date)
    #         print("TEXT: ", tweet.text, "LOCATION: ", tweet.geo, "INTERACTION: ", tweet.favorites, tweet.retweets)
    open_and_read_txt('/Users/ericlemmon/Downloads/2018_11_07_14_onepercent.txt')



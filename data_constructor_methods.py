import opener_methods
import pickle
from datetime import datetime
import json
import io


def pickle_data_contructor(FILE_NAME):
    tweets = opener_methods.open_and_read_pickle(FILE_NAME)
    now = datetime.now()
    date_time_string = now.strftime("%m%d%Y_%H%M%S")
    data = {}
    for date in tweets:
        try:
            data[date[0].date] = {
                # "geotags": [tweet.geo for tweet in date],
                "engagement": tweet_engagement_total(date),
                "no_top_tweets": len(date),
                "top_tweet_txt": find_top_tweet(date)
            }
        except:
            pass
    jar = open(date_time_string + ".dat", 'ab+')
    pickle.dump(data, jar)
    jar.close()

def json_data_contructor(FILE_NAME):
    tweets = opener_methods.open_and_read_pickle(FILE_NAME)
    now = datetime.now()
    date_time_string = now.strftime("%m%d%Y_%H%M%S")
    data = {}

    for date in tweets:
        try:
            data[date[0].date.strftime("%Y%m%d")] = {
                # "geotags": [tweet.geo for tweet in date],
                "engagement": tweet_engagement_total(date),
                "no_top_tweets": len(date),
                "top_tweet_txt": find_top_tweet(date)
            }
        except:
            pass

    with io.open(date_time_string + ".json", 'w', encoding='utf8') as outfile:
        string = json.dumps(data,
                         indent=4, sort_keys=True,
                         separators=(',', ': '), ensure_ascii=False)
        outfile.write(string)



def tweet_engagement_total(date):
    no_favs_retweets = 0
    for tweet in date:
        no_favs_retweets += tweet.favorites + tweet.retweets
    return no_favs_retweets

def find_top_tweet(date):
    top_tweet = date[0]
    for tweet in date:
        if tweet.favorites + tweet.retweets > top_tweet.favorites + top_tweet.retweets:
            top_tweet = tweet
        else:
            pass
    return {
        "username": top_tweet.username,
        "text": top_tweet.text,
        "engagement": top_tweet.favorites+top_tweet.retweets
    }

def get_engagement_min_and_engagement_max(tweets):
    max = tweets[0]['engagement']
    min = tweets[0]['engagement']
    for date in tweets:
        if tweets[date]['engagement'] > max:
            max = tweets[date]['engagement']
        if tweets[date]['engagement'] < min:
            min = tweets[date]['engagement']
    return (min, max)


if __name__ == "__main__":
    FILE_NAME = "old_top_tweets_dat.dat"
    pickle_data_contructor(FILE_NAME)
    json_data_contructor(FILE_NAME)



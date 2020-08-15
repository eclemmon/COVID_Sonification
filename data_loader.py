from opener_methods import open_and_read_pickle, open_and_read_json

"""
Currently the data is organized as follows:
01122020: {
'engagement': 1, # The total number of retweets and favourites on COVID related top tweets for the day
'no_top_tweets': 1, # The number of 'top tweets" for the day
'top_tweet_txt': { # This is the tweet that had the most engagement for the day
    'engagement': 1, # This is the amount of engagement that this best tweet got
    'text': '1. Raven Guy 2. Cham 3. 4 / 10 4. Ye, also I like you funky EPs, EP2 Song 6 got a laugh out of me. 5. Covid Pal 6. Nope 7. ', 
    'username': 'Capital_EKS' # This is the username of the person who wrote the most interacted with tweet.
    }
}


"""

def pickle_data_loader(FILE_NAME):
    return open_and_read_pickle(FILE_NAME)

def json_data_loader(FILE_NAME):
    return open_and_read_json(FILE_NAME)


if __name__ == "__main__":
    FILE_NAME = "04222020_150111.json"
    tweet_dict = json_data_loader(FILE_NAME)
    for key in tweet_dict:
        print(key, tweet_dict[key])
import GetOldTweets3
import pickle
import datetime, time
from date_incrementer import daterange

date_upper = datetime.date(2020, 4, 14)
date_lower = datetime.date(2019, 12, 1)

start_string = date_upper.strftime("%Y-%m-%d")
until_string = date_lower.strftime("%Y-%m-%d")

range = list(daterange(date_lower, date_upper))
print(range[:])

for index, date in enumerate(range):
    print(date)
    tweetCriteria = GetOldTweets3.manager.TweetCriteria().setQuerySearch("COVID") \
        .setMaxTweets(10000) \
        .setLang("en") \
        .setTopTweets(True) \
        .setSince(str(range[index-1]))\
        .setUntil(str(date))
    print('--- Starting query... ---')
    tweets = GetOldTweets3.manager.TweetManager.getTweets(tweetCriteria)
    print('--- Adding to list... ---')
    res = [tweet for tweet in tweets]
    print('--- Writing to Pickle File... ---')
    jar = open("old_top_tweets_dat.dat", 'ab+')
    pickle.dump(res, jar)
    jar.close()
    print('--- Going to sleep... ---\n\n')
    time.sleep(5*60)

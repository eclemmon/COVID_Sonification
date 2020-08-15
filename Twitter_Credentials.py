"""
This File builds the the json file that we store our credentials in. Enter your consumer key, consumer
secret, access token, and access secret after their respective dictionary keys in a string format
"""


import json

credentials = {}

credentials['CONSUMER_KEY'] = 'ENTER CONSUMER KEY HERE'
credentials['CONSUMER_SECRET'] = 'ENTER CONSUMER SECRET HERE'
credentials['ACCESS_TOKEN'] = 'ENTER ACCESS TOKEN HERE'
credentials['ACCESS_SECRET'] = 'ENTER ACCESS SECRET HERE'

with open('twitter_credentials.json', "w") as file:
    json.dump(credentials, file)
from gtts import gTTS
from data_loader import json_data_loader

def text_to_speech_generator(text, file_path):
    language = "en"
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(file_path + '.mp3')

if __name__ == "__main__":
    FILE_NAME = "04222020_150111.json"
    PATH = "/Users/ericlemmon/Google Drive/My Projects/Music Projects/Covid_Fly_Tweet_Twitter_Scraper/text_to_speech_files/"
    tweet_dict = json_data_loader(FILE_NAME)
    # for key in tweet_dict:
    #     print(key, tweet_dict[key]['top_tweet_txt']['text'])

    for key in tweet_dict:
        path = PATH + "{}".format(key)
        text = tweet_dict[key]['top_tweet_txt']['text']
        text_to_speech_generator(text, path)

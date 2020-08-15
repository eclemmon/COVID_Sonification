from data_loader import json_data_loader
from pythonosc import udp_client
from pythonosc import osc_message_builder
import time

client = udp_client.SimpleUDPClient("127.0.0.1", 57120)
FILE_NAME = "data_files/04222020_150111.json"
tweet_dict = json_data_loader(FILE_NAME)


for date in tweet_dict:
    msg = osc_message_builder.OscMessageBuilder(address='/s_new')
    msg.add_arg('rate', arg_type='s')
    print(tweet_dict[date]['engagement'])
    msg.add_arg(tweet_dict[date]['engagement'], 'i')
    msg = msg.build()
    client.send(msg)
    time.sleep(30/69)

# End the whole process
msg = osc_message_builder.OscMessageBuilder(address='/s_new')
msg.add_arg('false', arg_type='s')
msg.add_arg(1, arg_type='i')
msg = msg.build()
client.send(msg)
time.sleep(10)


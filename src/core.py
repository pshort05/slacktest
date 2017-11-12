# -*- coding: utf-8 -*-

import configparser
import logging
import json
from slackclient import SlackClient

# Setup Logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

config = configparser.ConfigParser()
config.read('slacktest.ini')
apitoken = config.get('slack', 'apitoken')

logging.debug("%s", apitoken)

slack = SlackClient(apitoken)

channels = slack.api_call("channels.list")
logging.debug("%s",channels)
with open('channels.json', 'w') as outfile:
    json.dump(channels, outfile)

channels = slack.api_call("channels.list")
logging.debug("%s",channels)
with open('channels.json', 'w') as outfile:
    json.dump(channels, outfile)
for channel_info in channels['channels']:
    logging.debug("%s", channel_info)
    if channel_info['is_channel']:
        history = slack.api_call("channels.history", channel=channel_info['id'])
        logging.debug("%s",history)
        with open('history.json', 'a') as outfile:
            json.dump(history, outfile)

users = slack.api_call("users.list")
logging.debug("%s",users)
with open('users.json', 'w') as outfile:
    json.dump(users, outfile)

for user_info in users['members']:
    logging.debug("%s", user_info)

conversations = slack.api_call("conversations.list",types="public_channel, private_channel")
logging.debug("%s", conversations)
with open('conversations.json', 'w') as outfile:
    json.dump('conversations.json', outfile)
for conversation_info in conversations['channels']:
    logging.debug("%s", conversation_info)
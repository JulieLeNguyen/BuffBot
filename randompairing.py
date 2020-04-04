# buff bot script to randomly pair people and create dm #

import os
import slack

slack_api_token = os.environ.get('slack_api_token')
print('slack_api_token')

client = slack.WebClient(token=os.environ.get('slack_api_token'))
response = client.chat_postMessage(
    channel='#botspam',
    text="Hellooo!")





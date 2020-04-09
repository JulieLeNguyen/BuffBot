# buff bot script to randomly pair people and create dm #

import os
import slack


slack_api_token = os.environ.get('slack_api_token')
print('slack_api_token')

#client = slack.WebClient(token=os.environ.get('slack_api_token'))
#response = client.chat_postMessage(
  #  channel='#buff',
   # text="testingg!")

slack_token = os.environ["slack_api_token"]
client = slack.WebClient(slack_token)

rolecall= client.conversations_members(channel="C0113BP18RG")

print (rolecall)

#group_open , create group dm
#im_created, dm was created
#message.im message posted in direct channel



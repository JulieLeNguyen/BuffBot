# buff bot script to randomly pair people and create dm #

import os
import slack
import random

slack_api_token = os.environ.get('slack_api_token')
#print(slack_api_token)
client = slack.WebClient(token=os.environ.get('slack_api_token'))

# to message in a channel
#response = client.chat_postMessage(
 #   channel='#buff',
  #  text="testingg!")

#find bot ID
bot_info=client.bots_info()
print(bot_info)

# to get list of members in channel
rolecall= client.conversations_members(channel="C0113BP18RG")['members']
print(rolecall)

#next step, generate 2 indices and then grab people from those indices

length=int(len(rolecall))
print(length)

firsthalf=rolecall[:length//2]
secondhalf=rolecall[length//2:]
#print(firsthalf)
#print(secondhalf)

#dming the pairs
#buff bot userid is U010T61DN0H
howdy=client.conversations_open(users=["UD86L3M54","U23L9EKQ8"])
print(howdy)

response = client.chat_postMessage(
    channel='G011KGP5YTY',
    text="Hello! It's time to get buff! (this is a test)")

#workout list

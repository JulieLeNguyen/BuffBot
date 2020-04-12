# buff bot script to randomly pair people and create dm #

import os
import slack
import random

slack_api_token = os.environ.get('slack_api_token')
#print(slack_api_token)
client = slack.WebClient(token=os.environ.get('slack_api_token'))

# to message in a channel
#response = client.chat_postMessage(
   #channel='#buff',
    #text="this isnt one punch man lmao")

# to get list of members in channel
rolecall= client.conversations_members(channel="C0113BP18RG")['members']
print(rolecall)

#next step, generate 2 indices and then grab people from those indices

length=int(len(rolecall))
print(length)

firsthalf=rolecall[:length//2]
secondhalf=rolecall[length//2:]

#buff bot userid is U010T61DN0H
del secondhalf[5]

print("firsthalf:",firsthalf)
print("secondhalf",secondhalf)

#get channel id from a pair

howdy=client.conversations_open(users=[random.choice(firsthalf),random.choice(secondhalf)])
print(howdy)

#workout list
workout_list=[
    '1 mile jog',
    'take a walk around campus',
    '50 situps',
    'go swinging!',
    'piggyback up and down floor',
    'run up to ehouse and back down to csh',
    'go for a bike/long board ride',
    'try rock climbing',
    '50 squats',
    '30 pushups',
    'play some ping pong',
    'do 5 jumping jacks every time you hear thinkpads'
]

workout1=random.choice(workout_list)
workout2=random.choice(workout_list)
workout3=random.choice(workout_list)

#message pair
response = client.chat_postMessage(
   channel=howdy['channel']['id'],
   text="Hello! It's time to get *buff*! _(this is a test)_ \n"
         "Your workout options are:\n>" +workout1 + "\n>" +workout2 + "\n>" +workout3)

#checking in
#response = client.chat_postMessage(
    #channel=
    #text= "Checking in! Did you get a chance to workout?"
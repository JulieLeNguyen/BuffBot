# buffbot script to randomly pair people and create dm #

import os
import slack
import random

slack_api_token = os.environ.get('slack_api_token')
buff_channel_id = os.environ.get('buff_channel_id')
buffbot_id=os.environ.get('buffbot_id')
#print(slack_api_token)
#print(buff_channel_id)
#print(buffbot_id)
client = slack.WebClient(token=os.environ.get('slack_api_token'))

# to message in a channel
#response = client.chat_postMessage(
   #channel='#buff',
    # text="testing!")

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
    'do 5 jumping jacks every time you hear thinkpads',
    'try out a weightlifting session',
    'plank competition',
    '15 burpees',
    '2 mile run'
]

# get list of members in channel
rolecall= client.conversations_members(channel=buff_channel_id)['members']
#print(rolecall)

random.shuffle(rolecall)
print("list after shuffle:", rolecall)

#del buffbot from users in channel
botindex=rolecall.index(buffbot_id)
#print(botindex)
del rolecall[botindex]

#generate 2 lists
length=int(len(rolecall))
#print(length)
firsthalf=rolecall[:length//2]
secondhalf=rolecall[length//2:]
#print("firsthalf:",firsthalf)
#print("secondhalf",secondhalf)

#slide into those dms
if (length %2)==0:
    max = len(firsthalf)
    n = 0
    while n < max:
        warmup = client.conversations_open(users=[firsthalf[n], secondhalf[n]])
        response = client.chat_postMessage(
            channel=warmup['channel']['id'],
            text="Hello! It's time to get *buff*! _(this is a test)_ \n"
                  "Your workout options are:\n>" +random.choice(workout_list) + "\n>" +random.choice(workout_list) + "\n>" +random.choice(workout_list))
        n += 1
else:
    max = len(secondhalf)
    print(max)
    n=0
    while n<max-2:
        warmup = client.conversations_open(users=[firsthalf[n], secondhalf[n]])
        response = client.chat_postMessage(
           channel=warmup['channel']['id'],
           text="Hello! It's time to get *buff*! _(this is a test)_ \n"
                "Your workout options are:\n>" +random.choice(workout_list) + "\n>" +random.choice(workout_list) + "\n>" +random.choice(workout_list))
        n += 1
    warmup = client.conversations_open(users=[firsthalf[max-2], secondhalf[max-2], secondhalf[max-1]])
    response = client.chat_postMessage(
        channel=warmup['channel']['id'],
        text="Hello! It's time to get *buff*! _(this is a test)_ \n"
             "Your workout options are:\n>" + random.choice(workout_list) + "\n>" +random.choice(workout_list) + "\n>" +random.choice(workout_list))

#checking in
if (length %2)==0:
    max = len(firsthalf)
    m = 0
    while m < max:
        warmup = client.conversations_open(users=[firsthalf[m], secondhalf[m]])
        response = client.chat_postMessage(
            channel=warmup['channel']['id'],
            text="Checking in! Did you get a chance to meet?"
                 m +=1
else:
    max = len(secondhalf)
    print(max)
    m=0
    while m<max-2:
        warmup = client.conversations_open(users=[firsthalf[m], secondhalf[m]])
        response = client.chat_postMessage(
           channel=warmup['channel']['id'],
           text="Checking in!"
           m += 1
    warmup = client.conversations_open(users=[firsthalf[max-2], secondhalf[max-2], secondhalf[max-1]])
    response = client.chat_postMessage(
        channel=warmup['channel']['id'],
        text="Checking in! Did you get a chance to meet?"
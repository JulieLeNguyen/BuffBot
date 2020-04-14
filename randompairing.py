# buffbot script to randomly pair people and create dm #

import os
import slack
import random

#environment variables!
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
w=open("workoutslist.txt", "r")
workouts= w.readlines()
#print(random.choice(workouts))

# get list of members in channel
rolecall= client.conversations_members(channel=buff_channel_id)['members']
#print(rolecall)

random.shuffle(rolecall)
#print("list after shuffle:", rolecall)

#del buffbot from users in channel
botindex=rolecall.index(buffbot_id)
#print(botindex)
del rolecall[botindex]

#generate 2 lists from users in channel
length=int(len(rolecall))
#print(length)
firsthalf=rolecall[:length//2]
secondhalf=rolecall[length//2:]
#print("firsthalf:",firsthalf)
#print("secondhalf",secondhalf)

#slide into those dms
#check if we have odd or even number amount of people in the channel
if (length %2)==0: #even scenario
    max = len(firsthalf)
    n = 0
    while n < max:
        warmup = client.conversations_open(users=[firsthalf[n], secondhalf[n]])
        response = client.chat_postMessage(
            channel=warmup['channel']['id'],
            text="Hello! It's time to get *buff*! _(this is a test)_ \n"
                  "Your workout options are:\n>" +random.choice(workouts) + "\n>" +random.choice(workouts) + "\n>" +random.choice(workouts))
        n += 1
else: #odd
    max = len(secondhalf)
    n=0
    while n<max-2:
        warmup = client.conversations_open(users=[firsthalf[n], secondhalf[n]])
        response = client.chat_postMessage(
           channel=warmup['channel']['id'],
           text="Hello! It's time to get *buff*! _(this is a test)_ \n"
                "Your workout options are:\n>" +random.choice(workouts) + "\n>" +random.choice(workouts) + "\n>" +random.choice(workouts))
        n += 1
    warmup = client.conversations_open(users=[firsthalf[max-2], secondhalf[max-2], secondhalf[max-1]]) #group of 3
    response = client.chat_postMessage(
        channel=warmup['channel']['id'],
        text="Hello! It's time to get *buff*! _(this is a test)_ \n"
             "Your workout options are:\n>" + random.choice(workouts) + "\n>" +random.choice(workouts) + "\n>" +random.choice(workouts))

#checking in
if (length %2)==0:
    max = len(firsthalf)
    m = 0
    while m < max:
        warmup = client.conversations_open(users=[firsthalf[m], secondhalf[m]])
        response = client.chat_postMessage(
            channel=warmup['channel']['id'],
            text="Checking in! Did you get a chance to meet?")
        m += 1
else:
    max = len(secondhalf)
    m=0
    while m<max-2:
        warmup = client.conversations_open(users=[firsthalf[n], secondhalf[n]])
        response = client.chat_postMessage(
            channel=warmup['channel']['id'],
            text="Checking in! Did you get the chance to meet?")
        m += 1
    warmup = client.conversations_open(users=[firsthalf[max-2], secondhalf[max-2], secondhalf[max-1]])
    response = client.chat_postMessage(
        channel=warmup['channel']['id'],
        text="Checking in! Did you get the chance to meet?")


#closing workoutslist.txt
w=open("workoutslist.txt", "r")
print(w.readline())

#to add in the future:
# specific day(s) to pair people and when to check in
# post in channel how many people met
# maybe add leaderboards if pairs do extra workout options?
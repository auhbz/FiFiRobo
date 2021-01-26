import discord
import os
import requests
import json
import random

client = discord.Client()

gr0 = ["Hello ", "Howdy ", "Hey ", "Greetings ", "Salutations ", "Whatup ", "So nice to hear from you ", "It's a pleasure to see you "]

gr1 = ["my lovely little lemon drop!!", "Carven!!", "my little hamster!!", "my precious angel!!", "my beautiful girl!!", "Howdy my special cutie pie!!", "my super duper peepee pooper!!"]

gr2 = [" :) ", " :D ", " ^-^ ", " c: ", " :> ", "  :] "]

gr3 = ["How may I serve you today?", "What's going on?", "How can I help?", "What would you like?"]

def get_hug():
  response = requests.get("https://some-random-api.ml/animu/hug")
  json_data = json.loads(response.text)
  hug = json_data['link']
  return hug

def get_pat():
  response = requests.get("https://some-random-api.ml/animu/pat")
  json_data = json.loads(response.text)
  pat = json_data['link']
  return pat

def get_meme():
  response = requests.get("https://meme-api.herokuapp.com/gimme")
  json_data = json.loads(response.text)
  meme = json_data['url']
  return meme

@client.event
async def on_ready():
  print('We are ready, user {0.user}'.format(client))

@client.event
async def on_message(message):
  msg = message.content.lower()

  if message.author == client.user:
    return
  
  if msg.startswith('hi fifi') or msg.startswith('hello fifi'):
    pat = get_pat()
    await message.channel.send(pat+" "+random.choice(gr0)+random.choice(gr1)+random.choice(gr2)+random.choice(gr3))

  if msg.startswith('carven want hug'):
    hug = get_hug()
    await message.channel.send(hug)

  if msg.startswith('carven want meme'):
    meme = get_meme()
    await message.channel.send(meme)

  if msg.startswith('carven want package'):
    mega = os.getenv('MEGA')
    await message.channel.send(mega)
    
client.run(os.getenv('TOKEN'))

#I'm thinking that I might just download a bunch of images instead of hitting an api to produce them... not sure. (for hamsters specifically)

##TODO:
#(last)!info - lists commands and functionality 
#(ready)!help - are you having anxiety? -> gives advice to calm down 
#baby bubba?
#!wisdom - sends zen/stoic quotes
#!package - sends emergency care package
#!hamster - sends random hamster images
#(DONE) !hug - sends random hug gifs
#!memories - sends random nice memories
#!sounds
#!vids
#!drive
#!cute
##
#do the ping thing so the bot stays awake indefinitely
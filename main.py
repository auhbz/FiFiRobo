import discord
import os
import requests
import json

client = discord.Client()

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
  if message.author == client.user:
    return
  
  if message.content.startswith('!hi') or message.content.startswith('!hello'):
    pat = get_pat()
    await message.channel.send(pat + " Hello my lovely little lemon drop!! How may I serve you today? :)")

  if message.content.startswith('!hug'):
    hug = get_hug()
    await message.channel.send(hug)

  if message.content.startswith('!meme'):
    meme = get_meme()
    await message.channel.send(meme)

client.run(os.getenv('TOKEN'))

#I'm thinking that I might just download a bunch of images instead of hitting an api to produce them... not sure.

##TODO:
#!info - lists commands and functionality 
#!help - are you having anxiety? -> gives advice to calm down 
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
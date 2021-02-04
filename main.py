import discord
import os
import requests
import json
import random

client = discord.Client()

gr0 = ["Hello ", "Howdy ", "Hey ", "Greetings ", "Salutations ", "Whatup ", "So nice to hear from you ", "It's a pleasure to see you "]

gr1 = ["my lovely little lemon drop!!", "Carven!!", "my little hamster!!", "my precious angel!!", "my beautiful girl!!", "Howdy my special cutie pie!!", "my super duper peepee pooper!!", "baby bubba!!"]

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
    await message.channel.send("\n\n**use the 'carven want info' command to learn what I can do!**")

  if msg.startswith('carven want hug'):
    hug = get_hug()
    await message.channel.send(hug)

  if msg.startswith('carven want meme'):
    meme = get_meme()
    await message.channel.send(meme)

  if msg.startswith('carven want package'):
    mega = os.getenv('MEGA')
    await message.channel.send(mega)
  
  if msg.startswith('carven want help'):
    await message.channel.send("LOVE!!! Are you having anxiety? Is your chest hurting? Whatever is going on, I'm here to help! :D\n\n`1) focus on your breathing`\n`2) realize this will pass and if theres pain it is likely due to stress`\n`3) its all in your head, you can control it`\n`4) Focus. On. Your. Breathing`\n`5) look at hamsters, potato trump, memes`\n`6) find my hoody and cuddle with it 7) stay hydrated!`\n\nDon't forget to use my commands to help you out if needed :)\n\n**Finally, Remember:**\nThis bot itself is something i made out of love and care for you. Even though I might not always be at my best, this bot will... even if i might not be around or awake all the time, this bot will... let it be a happy thing, a comforting thing, a reminder of the love and care i feel for you -Auhbon")
  
  if msg.startswith("carven want info"):
    info_msg = "`carven want ___` : This is how you give me commands!\n\nHere are some words to try!\n`hug`\n`meme`\n`package`\n\nTry them out to see what they do! :)\n\nOne special command that you should understand ahead of time is `help`. Use this when you're having anxiety, chest pain, or are otherwise freaking out and can't get ahold of auhbz <3"
    embed = discord.Embed(color = 0x00ff00)
    embed.title = "Info"
    embed.description = info_msg
    await message.channel.send(embed=embed)
    
client.run(os.getenv('TOKEN'))
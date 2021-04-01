import discord
import os
import requests
import json
import random
from googleapiclient.discovery import build
from keepalive import keep_alive

client = discord.Client()

mega = os.getenv('MEGA')
tenor = os.getenv("TENOR")
yt_key = os.getenv("YOUTUBE")

cmd = 'carven want '
gif_lmt = 8
youtube = build('youtube', 'v3', developerKey=yt_key)

wipmsg = "Whoopsie, this is a wip! But in the future, this will "

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

def get_memory():
  return wipmsg+"return a random happy memory that carven and auhbon shared!"

def get_pic():
  return wipmsg+"return a random pic (mostly hamsters)!"

def get_wisdom():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  wisdom = json_data[0]['q'] + " -" + json_data[0]['a']
  return wisdom

def get_mochi(search_term, index):
  response = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, tenor, gif_lmt))
 
  top_8gifs = json.loads(response.content)         
  url = top_8gifs['results'][index]['media'][0]['gif']['url']
  return url

# could I use the 'pageToken' parameter to get a true random?
#honestly.... i could just grab every single video id using the api then just do random choice on it... seems like a very easy alternative but also a lot less cool haha
def get_video():
  maxRe = 50
  request = youtube.playlistItems().list(part='contentDetails',playlistId='PL-pmgH6nZ_TPZXfF-jU-jYHItPHTuKCRC', maxResults=maxRe)
  json_data = request.execute()
  item = random.choice(json_data['items'])
  video = item['contentDetails']['videoId']
  return 'https://youtube.com/watch?v='+video

  # request = youtube.playlistItems().list(part='contentDetails',playlistId='PL-pmgH6nZ_TPZXfF-jU-jYHItPHTuKCRC')
  # # response = request.execute()
  # # json_data = json.loads(response.body)
  # json_data = request.execute()
  # vid = random.choice(json_data['items'])
  # video = "youtube.com/?v="+vid['contentDetails'][0]
  # return video

  # return wipmsg+"return a random video from the special youtube playlist i made for carven!"
  #playlistItems.list returns

  #getting videoId from playlistItems.list() => contentDetails[0]

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

  if msg.startswith(cmd+'hug'):
    hug = get_hug()
    await message.channel.send(hug)

  if msg.startswith(cmd+'meme'):
    meme = get_meme()
    await message.channel.send(meme)

  if msg.startswith(cmd+'package'):    
    await message.channel.send(mega)
  
  if msg.startswith(cmd+'video'):
    video = get_video()
    await message.channel.send(video)

  if msg.startswith(cmd+'memory'):
    memory = get_memory()
    await message.channel.send(memory)

  if msg.startswith(cmd+'pic'):
    pic = get_pic()
    await message.channel.send(pic)

  if msg.startswith(cmd+'wisdom'):
    wisdom = get_wisdom()
    await message.channel.send(wisdom)

  if msg.startswith(cmd+'mochi'):
    search_term = msg.split(cmd+'mochi ',1)[1]
    index = random.randint(0,7)
    mochi = get_mochi(search_term, index)
    await message.channel.send(mochi)

  if msg.startswith(cmd+'help'):
    await message.channel.send("LOVE!!! Are you having anxiety?Is your chest hurting? Whatever is going on, I'm here to help! :D\n\n`1) focus on your breathing`\n`2) realize this will pass and if theres pain it is likely due to stress`\n`3) its all in your head, you can control it`\n`4) Focus. On. Your. Breathing`\n`5) look at hamsters, potato trump, memes`\n`6) find my hoody and cuddle with it \n7) stay hydrated!`\n`19)Repeat steps 1-7!!`\n\nDon't forget to use my commands to help you out further as needed :)\n\n**Finally, Remember:**\nThis bot itself is something i made out of love and care for you. Even though I might not always be at my best, this bot will... even if i might not be around or awake all the time, this bot will... let it be a happy thing, a comforting thing, a reminder of the love and care i feel for you -Auhbon <3")
  
  if msg.startswith(cmd+"info"):
    info_msg = "`carven want ___` : This is how you give me commands!\n\nHere are some words to try!\n`hug`\n`meme`\n`package`\n`video`\n`wisdom`\n`pic`\n`memory`\n`mochi ___`\n\nTry them out to see what they do! :)\n\nOne special command that you should understand ahead of time is `help`. Use this when you're having anxiety, chest pain, or are otherwise freaking out and can't get ahold of auhbz <3"
    embed = discord.Embed(color = 0x00ff00)
    embed.title = "Info"
    embed.description = info_msg
    await message.channel.send(embed=embed)
    
keep_alive()
client.run(os.getenv('TOKEN'))
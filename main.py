import discord
import asyncio
import random
import json
import time
import requests
from discord.ext import commands

import random

def openn():
    global Q, C
    Q = []
    C = []
    TOKEN = ''
    openn = open("savesBotNM.txt", "r")
    contenu = openn.read()
    text = []
    text = contenu.split("#...#", 3)
    #print(x,y)
    TOKEN = text[0]
    Q = text[1]
    C = text[2]
    Q = Q.split(",")
    C = C.split(",")
    #print(Q)
    #print(C)
    openn.close()
    return TOKEN ,Q ,C

def saves():
    global C, Q, TOKEN
    saves = open("savesBotNM.txt", "w+")
    text_Q = ''
    text_C = ''
    for text in Q:
        if text == Q[0]:
            text_Q = text_Q+str(text)
        else:
            text_Q = text_Q+','+str(text)
    for text in C:
        if text == C[0]:
            text_C = text_C+str(text)
        else:
            text_C = text_C+','+str(text)
    Q = str(text_Q)
    C = str(text_C)
    saves.write(TOKEN+'#...#'+str(Q)+"#...#"+str(C))
    saves.close()

TOKEN, Q, C= openn()
saves()

bot = commands.Bot(command_prefix=commands.when_mentioned_or('--'))

@bot.event
async def on_ready():
    print("Bot en ligne.")

@bot.command()
async def info(channel):
    await channel.send("Information du Bot_NM")
    
@bot.command()
async def ping(channel):
    await channel.send(":ping_pong: pong :rofl: :rofl:")

@bot.command()
async def blague(channel, message):
    if message == "liste":
      r = requests.get('https://blague.xyz/api/joke/list', headers={'Authorization': '42hJZfVD3-dOE29cRl5gQDmi8AE-6bIi-..ieIrudvX2pzOSgpmTHvpDJFf-X_9I'})
      print(r.json())
      message = "day"
    r = requests.get('https://blague.xyz/api/joke/{}'.format(message), headers={'Authorization': '42hJZfVD3-dOE29cRl5gQDmi8AE-6bIi-..ieIrudvX2pzOSgpmTHvpDJFf-X_9I'})
    r_dict = r.json()
    question = r_dict["joke"]["question"]
    reponse = r_dict["joke"]["answer"]
    await channel.send(question + ":smirk:\n" + "||" + reponse + " :sweat_smile: ||")
    #await channel.edit(question + "\n" + reponse + " :sweat_smile:")
    #await asyncio.sleep(2)
    #await channel.send(reponse + " :sweat_smile:")

@bot.command()
async def learnblague(channel, question, reponse):
    global Q, C
    await channel.send("Apprentissage de la blague !")
    print(question + 'yo' + reponse)
    Q.append(question)
    C.append(reponse)
    saves()
    await channel.send("Blague bien apprise!!")

@bot.command()
async def blague_apprise(channel):
  TOKEN, Q, C = openn()
  max_Q = len(Q)-1
  alea = random.randint(0,max_Q)
  #print(max_Q,'\n',alea)
  await channel.send(Q[alea] + ":smirk:\n" + "||" + C[alea] + " :sweat_smile: ||")

try:
    bot.run(TOKEN)
except ImportError:
    print("ne faite pas ca !!!!!!")

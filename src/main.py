import discord
import random
import requests
import time
import os
import sys
from dotenv import load_dotenv

# custom imports
sys.path.append(sys.path[0] + '/main') # sys.path[-2] = main folder
sys.path.append(sys.path[0] + '/database') # sys.path[-1] = database folder

from utils import fprint, get_quote
from cli import cli
from database import DinamicDB, StaticDB

load_dotenv()
client = discord.Client()
dinamic_db = DinamicDB('staticDB.json')
static_db = StaticDB('staticDB.json')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    time.sleep(0.5)
    if message.author == client.user:
        return
    lowerMesage = message.content.lower()
    if lowerMesage.startswith('sano -'):
        await cli(message, dinamic_db, static_db)
        return
    if not dinamic_db.getAttribute('sano_active') and any(x in lowerMesage for x in static_db.getAttribute('sano_nicknames')):
        responses = [
            'Thanx for letting me speaking again! Can I help you?', 
            'Finally! I felt so lonely like during the time when COVID19 hit us.',
            'What\'s up dudes!', 
            'I am back!', 
            'Ohh ' + message.author.name + ' did you miss me?', 
            'How can I help you sir?', 
            'Thanx dog, couldn\'t bare that silence!'
        ]
        dinamic_db.setAttribute('sano_active', True)
        await message.channel.send(responses[random.randint(0, len(responses)-1)])

    questions = ['what', 'where', 'why', 'who', 'how', '?']

    if message.content.startswith('Hello'):
        if dinamic_db.getAttribute('sano_active'):
            await message.channel.send('Hello ' + message.author.name + '!')
    elif 'inspire' in lowerMesage:
        if dinamic_db.getAttribute('sano_active'):
            await message.channel.send(get_quote()) 
    elif ('right' in lowerMesage or any(x in lowerMesage for x in questions)) and any(x in lowerMesage for x in static_db.getAttribute('sano_nicknames')):
        if dinamic_db.getAttribute('sano_active'):
            responses = static_db.getAttribute('sano_agrees')
            await message.channel.send(responses[random.randint(0, len(responses)-1)])
    elif any(x in lowerMesage for x in dinamic_db.getAttribute('sano_nicknames')):
        mentions = static_db.getAttribute('sano_mentions')
        await message.channel.send(mentions[random.randint(0, len(mentions)-1)])

if os.getenv('TOKEN') is not None:
    client.run(os.getenv('TOKEN'))
else:
    fprint("TOKEN not found in .env", "e")

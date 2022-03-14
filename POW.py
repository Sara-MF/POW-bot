import discord
import time
import random
import os
from discord.ext import commands

client = discord.Client()

bot = commands.Bot

on = True

# liga o bot
@client.event
async def on_ready():
    print('I am running')

# recebe a palavra
@client.event
async def on_message(message):

    # deixa a palavra pow em uppercase
    message.content = message.content.upper()

    global on

    # não permite que o bot se dispare sozinho quando ele mesmo mandar o POW
    if message.author == client.user:
        return
    
    # o bot é disparado entre 15 e 45 min
    if message.content.startswith('POW'):
        while(on):
            await message.channel.send(':fireworks:  POW POW ROW POW POW  :fireworks:')
            time.sleep(15)
            await message.channel.send('...POW!  :fireworks:')
            time.sleep(random.randint(900, 2700))


    if message.content.startswith('PARE'):
        on = False

# token do bot
bot.run(os.getenv('TOKEN'))

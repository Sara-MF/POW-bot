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
            time.sleep(2)
            # time.sleep(15)
            await message.channel.send('...POW!  :fireworks:')
            time.sleep(random.randint(5, 10))
            # time.sleep(random.randint(900, 2700))


    if message.content.startswith('PARE'):
        on = False

client.run('OTUyNjMyODA4OTUyNzI1NTc0.Yi42cA.UTnXXC33ksSo2OVDKrokQPjlyqI')
# bot.run(os.getenv('TOKEN'))

"""

# Pra restartar o bot
import os
from discord.ext import commands

bot = commands.Bot

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@bot.command(name= 'restart')
async def restart(ctx):
  await ctx.send("Restarting bot...")
  restart_bot()

# Pra desligar o bot
@client.command(aliases=["quit"])
@commands.has_permissions(administrator=True)
async def close(ctx):
    await client.close()
    print("Bot Closed")  # This is optional, but it is there to tell you.

"""


"""
# MEU BOT ANTES DOS COMANDOS DE DESLIGAMENTO


import discord
import time
import random

on = True

client = discord.Client()

@client.event
async def on_ready():
    print('I am ready')

@client.event
async def on_message(message):

    message.content = message.content.upper()

    global on

    if message.author == client.user:
        return
    
    if message.content.startswith('QUEIMA'):
        while(on):
            await message.channel.send(':fireworks:  POW POW ROW POW POW  :fireworks:')
            time.sleep(2)
            # time.sleep(15)
            await message.channel.send('...POW!  :fireworks:')
            time.sleep(random.randint(5, 10))
            # time.sleep(random.randint(900, 2700))


    if message.content.startswith('PARE'):
        on = False

client.run('OTM3MDg4ODY1MjIxNjI3OTU1.YfWqAw.7nfrj6MERysZ19I-X3rWQsbf9jI')

"""








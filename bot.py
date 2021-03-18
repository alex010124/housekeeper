import discord
from discord.ext import commands
import json
import random
import os

with open('setting.json' , mode = 'r' , encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix="[")

@bot.event
async def on_ready():
    print(">> Bot is online <<")



for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(f'cmds.{Filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
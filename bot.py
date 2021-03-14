import discord
from discord.ext import commands
import json
import random

with open('setting.json' , mode = 'r' , encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix="[")

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms')

@bot.command()
async def 圖片(ctx):
    pic = discord.File(jdata['PIC'])
    await ctx.send(file = pic)






bot.run(jdata['TOKEN'])
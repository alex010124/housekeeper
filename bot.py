import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="[")

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    print(f'{member} join!')
    channel = bot.get_channel('820742681507659776')
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')
    channel = bot.get_channel('820742719012995102')
    await channel.send(f'{member} leave!')

bot.run('ODE3NjU5Njg0OTk4NjEwOTg2.YEMu7A.bSvN2o_mKVow0mOVTPiDnMKaKzI')
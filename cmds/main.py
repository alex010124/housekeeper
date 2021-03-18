import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import json

with open('setting.json' , mode = 'r' , encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} ms')

    @commands.command()
    async def sayd(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title="about", description="about housekeeper", color=0x00fbff, timestamp= datetime.datetime.now())
        embed.set_author(name="Sheng")
        embed.add_field(name="1", value="11", inline=False)
        embed.add_field(name="2", value="22", inline=False)
        embed.add_field(name="3", value="33", inline=False)
        embed.add_field(name="4", value="44", inline=False)
        await ctx.send(embed=embed)
    
    

def setup(bot):
    bot.add_cog(Main(bot))
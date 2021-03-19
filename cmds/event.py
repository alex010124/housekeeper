import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json' , mode = 'r' , encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['LEAVE_CHANNEL']))
        await channel.send(f'{member} leave!')
        
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == 'apple' and msg.author != self.bot.user:
            await msg.channel.send('apple')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        print(payload.emoji)
        if payload.message_id == 822355740181790790:
            if str(payload.emoji) == '<:cha:814150233784451143>':
                guild = self.bot.get_guild(payload.guild_id)
                role = guild.get_role(691293603120807949)
                await payload.member.add_roles(role)
                await payload.member.send(f"you get {role}")
            elif str(payload.emoji) == '<:leon:695249835045027913>':
                guild = self.bot.get_guild(payload.guild_id)
                role = guild.get_role(787619351326883840)
                await payload.member.add_roles(role)
                await payload.member.send(f"you get {role}")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == 822355740181790790:
            if str(payload.emoji) == '<:cha:814150233784451143>':
                guild = self.bot.get_guild(payload.guild_id)
                user = await guild.fetch_member(payload.user_id)
                role = guild.get_role(691293603120807949)
                await user.remove_roles(role)   
                await user.send(f"you remove{role}")
            elif str(payload.emoji) == '<:leon:695249835045027913>':
                guild = self.bot.get_guild(payload.guild_id)
                user = await guild.fetch_member(payload.user_id)
                role = guild.get_role(787619351326883840)
                await user.remove_roles(role)   
                await user.send(f"you remove{role}")

def setup(bot):
    bot.add_cog(Event(bot))

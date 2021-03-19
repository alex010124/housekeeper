import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json , asyncio , datetime

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

#        async def interval():
#            await selt.bot.wait_until_ready()
#            self.channel = self.bot.get_channel()
#            while not self.bot.is_closed():
#                await self.channel.send("hi")
#                await asyncio.sleep(5)
#            self.bg_task = self.bot.loop.create_task(interval())    






def setup(bot):
   bot.add_cog(Task(bot))
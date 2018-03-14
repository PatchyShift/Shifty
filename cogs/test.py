import discord
from discord.ext import commands

class test:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self):

        #Your code will go here
        await self.bot.say("This is a test!")

def setup(bot):
    bot.add_cog(test(bot))
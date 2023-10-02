
from discord.ext import commands
from colorama import Fore, init
import time

# Command Description: test

init(autoreset=True)

class testCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def test(self, ctx):
        await ctx.send("Hello!")



async def setup(bot):
    await bot.add_cog(testCommand(bot))



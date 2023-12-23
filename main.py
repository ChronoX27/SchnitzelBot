from bot_slashcommands import Slashcommands
from bot_commands import Commands
import dotenv
import os
import discord
import functions
from discord.ext import commands


dotenv.load_dotenv()

status = str(os.getenv("status"))
prefix = str(os.getenv("prefix"))
intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix=prefix, intents=intents, activity=discord.Game(name=status)
)


bot.add_cog(Commands(bot))
bot.add_cog(Slashcommands(bot))


@bot.event
async def on_ready():
    functions.ready(bot)


functions.keep_alive()
bot_token = str(os.getenv("TOKEN"))
bot.run(bot_token)

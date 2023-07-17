import json
import dotenv
import os
import discord
import functions
from discord.ext import commands


with open("config.json") as data_file:
    config_data = json.load(data_file)

status = config_data["status"]
prefix = config_data["prefix"]
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents, activity=discord.Game(name=status))


from bot_commands import Commands
from bot_slashcommands import Slashcommands

bot.add_cog(Commands(bot))
bot.add_cog(Slashcommands(bot))


@bot.event
async def on_ready():
    functions.ready(bot)


functions.keep_alive()
dotenv.load_dotenv()
TOKEN = str(os.getenv(config_data["bot_token"]))
bot.run(TOKEN)
from bot_slashcommands import Slashcommands
from bot_commands import Commands
import dotenv
import os
import discord
import functions
from discord.ext import commands


dotenv.load_dotenv()

bot = commands.Bot(
    intents=discord.Intents.all(),
    command_prefix=str(os.getenv("prefix")),
    activity=discord.Game(name=str(os.getenv("status")))
)

bot.add_cog(Commands(bot))
bot.add_cog(Slashcommands(bot))

@bot.event
async def on_ready():
    functions.ready(bot)


bot_token = str(os.getenv("TOKEN"))
bot.run(bot_token)

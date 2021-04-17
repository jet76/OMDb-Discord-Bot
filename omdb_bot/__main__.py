import os

import discord

from discord.ext import commands
from discord.ext.commands import CommandNotFound
from dotenv import load_dotenv

from omdb import OMDb


description = '''OMDb Bot.'''

#intents = discord.Intents.default()
#intents.members = True

bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, CommandNotFound):
    return
  raise error


load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OMDB_API_KEY = os.getenv('OMDB_API_KEY')

bot.add_cog(OMDb(bot, OMDB_API_KEY))
bot.run(DISCORD_TOKEN)
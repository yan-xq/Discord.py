import discord
from discord.ext import commands

#intents
intents = discord.Intents.all()

#bot
bot = commands.Bot(command_prefix = '.', help_command=None, intents = intents)

#activity
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('your activity'))
   
#run
bot.run('your token')

import discord
from discord.ext import commands

#intents
intents = discord.Intents.all()

#bot
bot = commands.Bot(command_prefix = '.', help_command=None, intents = intents)

#system
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('.help'))
    print('connected')

@bot.command(aliases=['embed'])#aliases can rename your command
async def __embed(ctx):
    embed = discord.Embed(
        title='your title embed',
        description='your description',
        color=discord.Color.red()#you can choose another embed color
    )
    embed.add_field(name='your field name', value='your field description or value', inline='False or True')#field
    embed.set_footer(text='your text', icon_url='your link for icon')#footer
    embed.set_author(name='your author name and also you can write ctx.message.author', icon_url='your link for icon')#author
    embed.set_image(url='your link for image')#image
    embed.set_thumbnail(url='your link for image')#thumbnail
    await ctx.send(embed = embed)

bot.run('your token')

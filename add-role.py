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
    print('connected')

#add-role
@bot.command(aliases=['add role', 'role'])
async def __role(ctx, member: discord.Member):
    if member == None:
        user = ctx.message.author
        role = discord.utils.get(ctx.message.server.guild.roles, name='your role name')
        await user.add_roles(role)
        await ctx.send(f'User {user} got role: (role name)')

    else:
        role = discord.utils.get(ctx.message.server.guild.roles, name='your role name')
        await member.add_roles(role)
        await ctx.send(f'User {member} got role: (role name)')

#run
bot.run('your token')
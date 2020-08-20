import discord
import random2
import os

from discord.ext import commands

#@bot.command(pass_context=True) 
#async def test(ctx): 
#    await ctx.send('Дима лох')

bot = commands.Bot(command_prefix='!')

@bot.command(pass_context=True)
async def msg(ctx, *, arg):
    await ctx.send(arg) 

@bot.command(pass_context=True)   
async def h(ctx):
    await ctx.send('*Типо список комманд*')

@bot.command(pass_context=True)   
async def ban(ctx, user: discord.User):
    await ctx.send('Пользователь ' + user.name + ' забанен пользователем ' + format(ctx.message.author))

bot.run(str(os.environ.get('BOT_TOKEN')))

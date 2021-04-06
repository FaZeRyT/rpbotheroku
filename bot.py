import discord
import random2
import os

from discord.ext import commands



bot = commands.Bot(command_prefix='.')

@bot.command(pass_context=True)
async def msg(ctx, *, arg):
    await ctx.send(arg) 

@bot.command(pass_context=True)   
async def help(ctx):
    await ctx.send('```bash' + '\n' + '#Серый цвет' + '\n' + '"Бирюзовый"' + '\n' + '$Yellow```')

@bot.command(pass_context=True)   
async def safe(ctx, user: discord.User):
	await member.mention.add_roles(828868950569779210)
    await ctx.send('Пользователь ' + user.name + ' помечен как "Safe"')

@bot.command(pass_context=True)   
async def unsafe(ctx, user: discord.User):
	await member.mention.add_roles(828869017569591307)
    await ctx.send('Пользователь ' + user.name + ' помечен как "Unsafe"')

bot.run(str(os.environ.get('BOT_TOKEN')))

import discord
import discord.role
import random2
import os

from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.command(pass_context=True)
async def msg(ctx, *, arg):
    await ctx.send(arg) 

@bot.command(pass_context=True)   
async def test(ctx):
    await ctx.send('```bash' + '\n' + '#Серый цвет' + '\n' + '"Бирюзовый"' + '\n' + '$Yellow```')

@commands.has_permissions( administrator = True ) 
@bot.command(pass_context=True)   
async def clear(ctx, amount = 2):
	await ctx.channel.purge( limit = amount )

@bot.command(pass_context=True)   
@commands.has_permissions( administrator = True )
async def safe(ctx, user: discord.User):
    #await ctx.send(str(user.id) + '\n' + str(user))
    rolesafe = discord.utils.get( user.guild.roles, id = 828868950569779210 )
    roleunsafe = discord.utils.get( user.guild.roles, id = 828869017569591307 )
    await user.add_roles( rolesafe )
    await user.remove_roles( roleunsafe )
    await ctx.send('Роли ' + user.mention + ' обновлены.')

@bot.command(pass_context=True)
@commands.has_permissions( administrator = True )   
async def unsafe(ctx, user: discord.User):
    rolesafe = discord.utils.get( user.guild.roles, id = 828868950569779210 )
    roleunsafe = discord.utils.get( user.guild.roles, id = 828869017569591307 )
    await user.add_roles( roleunsafe )
    await user.remove_roles( rolesafe )
    await ctx.send('Роли ' + user.mention + ' обновлены.')

@bot.event
async def on_user_join( user ):

	role = discord.utils.get( user.guild.roles, id = 828988730312097834 )

	await user.add_roles( role )

bot.run(str(os.environ.get('BOT_TOKEN')))
import discord

#@bot.command(pass_context=True) 
#async def test(ctx): 
#    await ctx.send('Дима лох')

bot = commands.Bot(command_prefix='!')

@bot.command(pass_context=True)
async def msg(ctx, *, arg):
    await ctx.send(arg)  
    print('Сообщение с текстом "' + str(arg) + '" отправлено!')

@bot.command(pass_context=True)   
async def h(ctx):
    await ctx.send('*Типо список комманд*')
    print('Выведен список комманд.')

@bot.command(pass_context=True)   
async def ban(ctx, user: discord.User):
    await ctx.send('Пользователь ' + user.name + ' забанен пользователем ' + format(ctx.message.author))
    print(user.name + ' забанен!')

token = os.environ.get('BOT_TOKEN')
bot.run(str(token))
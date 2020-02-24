import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command(pass_context=True)
async def msg(ctx, *, arg):
    await ctx.send(arg)  

@bot.command(pass_context=True)
async def h(ctx):
	await ctx.send('gexp (Игрок) (Кол-во) - Выдача опыта (Система уровней)' + '\n' + 'gmoney (Игрок) (Кол-во) - Выдача денег (Экономика)' + '\n' + 'rptry - Попытать удачу, шанс 50% (РП)' + '\n' + 'rprnd (Игрок) - Случайное число от 1 до 9 (РП)' + '\n' + 'dmg (Игрок) (Урон) - Урон игроку (РП)' + '\n' + 'heal (Игрок) (Кол-во) - Добавление единиц здоровья игроку (РП)' + '\n' + 'smoney (Игрок) (Кол-во) - Трата денег (Экономика)' + '\n' + 'pay (От кого) (Кому) (Кол-во) - Передача денег (Экономика)' + '\n' + 'stat (Игрок) - Просмотр всей информации о игроке (РП)' + '\n' + format(ctx.message.author.mention))

@bot.command(pass_context=True)   
async def rptry(ctx):
    if str(random.randint(1, 2)) == '2':
    	await ctx.send('Удача на вашей стороне ;) ')
    else:
    	await ctx.send('Вы потерпели неудачу :с ')

@bot.command(pass_context=True)   
async def rprnd(ctx, user: discord.User):
	rpint = str(random.randint(1, 9))
	await ctx.send('Выпало число: ' + rpint)
	if int(rpint) < 5:
		dmgs = '0'
		if str(rpint) == '4':
			if random.randint(1, 3) < 3:
				botmsg = ' промахнулся..'
			else:
				botmsg = ' потерпел неудачу, противник увернулся.'
		else:
			fint = '-' + rpint
			fint = int(fint) + 4
			if str(fint) == '1':
				dmgs = '10'
				botmsg = ' промахнулся и сделав оборот вокруг себя упал на землю. Эта неудача сняла у него 10 хп.'
			if str(fint) == '2':
				dmgs = '20'
				botmsg = ' упал на что-то острое, поранившись он потерял 20 хп..'
			if str(fint) == '3':
				dmgs = '50'
				fint = random.randint(1, 9)
				if fint < 9:
					if str(random.randint(1, 2)) == '2':
						botmsg = ' не успев ударить противника замечает летящий в него кирпич, он пытается увернуться, но кирпич прилетает ему в голову. -50 хп.'
					else:
						botmsg = ' попав в землю промахнулся по противнику, отскочивший от земли камень встречает на своём пути припятсвие и отскакивает в игрока.. -50 хп.'
				elif str(fint) == '9':
					botmsg = ' спотыкается и упав на камень теряет 0 хп..... Но подождите! Кажется этот камень.... ожил? Он взлетел и ударил игрока.. -50 хп.'
		hp1f = open('rpb/players/' + user.name + '/hp.txt')
		hp1 = int(hp1f.read())
		hp1f.close()
		if int(dmgs) + 1 > int(hp1):
			await ctx.send('Игрок ' + user.name + botmsg + ' Игрок умер.. ' + format(ctx.message.author.mention))
			hp1f = open('rpb/players/' + user.name + '/hp.txt', 'w')
			hp1f.write('0')
			hp1f.close()
		else:
			hp1 = hp1 - int(dmgs)
			hp1f = open('rpb/players/' + user.name + '/hp.txt', 'w')
			hp1f.write(str(hp1))
			hp1f.close()
		await ctx.send('Игрок ' + user.name + botmsg + ' Теперь у него ' + str(hp1) + ' хп.')
	else:
		fint2 = int(rpint) - 4
		arg = 10 * int(fint2)
		expf = open('rpb/players/' + user.name + '/exp.txt')
		exp = int(expf.read())
		expf.close()
		exp = exp + int(arg)
		lvlf = open('rpb/players/' + user.name + '/lvl.txt')
		lvl = int(lvlf.read())
		lvlf.close()
		if exp + 1 > 100 + int(lvl) * 20:
			succ = '0'
			while succ != '1':
				expg = 100 + int(lvl) * 20
				exp = exp - expg
				lvl = int(lvl) + 1
				if exp + 1 > 100 + int(lvl) * 20:
					succ = '0'
				else:
					succ = '1'
			hpf = open('rpb/players/' + user.name + '/hp.txt')
			hp = int(hpf.read())
			hpf.close()
			hp = hp + 30
			hpf = open('rpb/players/' + user.name + '/hp.txt', 'w')
			hpf.write(str(hp))
			hpf.close()
			await ctx.send('Игрок ' + user.name + ' успешно совершив задуманное получил ' + str(arg) + ' опыта и новый уровень. Теперь у него ' + str(lvl) + ' лвл. +30 хп.')
		else:
			await ctx.send('Игрок ' + user.name + ' успешно совершив задуманное получил ' + str(arg) + ' опыта, теперь у него ' + str(exp) + ' опыта.')	
		expf = open('rpb/players/' + user.name + '/exp.txt', 'w')
		expf.write(str(exp))
		expf.close()
		lvlf = open('rpb/players/' + user.name + '/lvl.txt', 'w')
		lvlf.write(str(lvl))
		lvlf.close()

@bot.command(pass_context=True)   
async def gmoney(ctx, user: discord.User, arg):
	mof = open('rpb/players/' + user.name + '/money.txt')
	mo = int(mof.read())
	mof.close()
	mo = mo + int(arg)
	mof = open('rpb/players/' + user.name + '/money.txt', 'w')
	mof.write(str(mo))
	mof.close()
	await ctx.send('Игрок ' + user.name + ' получил ' + str(arg) + ' монет, теперь у него ' + str(mo) + ' монет.')

@bot.command(pass_context=True)   
async def dmg(ctx, user: discord.User, arg):
	hpf = open('rpb/players/' + user.name + '/hp.txt')
	hp = int(hpf.read())
	hpf.close()
	if int(arg) >= int(hp):
		await ctx.send('Игрок ' + user.name + ' умер, получив роковые ' + str(arg) + ' единиц урона.. ' + format(ctx.message.author.mention))
		hpf = open('rpb/players/' + user.name + '/hp.txt', 'w')
		hpf.write('0')
		hpf.close()
	else:
		hp = hp - int(arg)
		await ctx.send('Игрок ' + user.name + ' получил ' + str(arg) + ' единиц урона, теперь у него ' + str(hp) + ' хп.')
		hpf = open('rpb/players/' + user.name + '/hp.txt', 'w')
		hpf.write(str(hp))
		hpf.close()
	
@bot.command(pass_context=True)   
async def heal(ctx, user: discord.User, arg):
	hpf = open('rpb/players/' + user.name + '/hp.txt')
	hp = int(hpf.read())
	hpf.close()
	if str(hp) == '0':
		hpf = open('rpb/players/' + user.name + '/hp.txt', 'w')
		hpf.write(str(arg))
		hpf.close()
		await ctx.send('Игрок ' + user.name + ' возрадился с ' + str(arg) + ' хп.')
	else:
		hp = hp + int(arg)
		hpf = open('rpb/players/' + user.name + '/hp.txt', 'w')
		hpf.write(str(hp))
		hpf.close()
		await ctx.send('Игрок ' + user.name + ' отрегенирировался / подлечился, +' + str(arg) + ' хп, теперь у него ' + str(hp) + ' хп.')

@bot.command(pass_context=True)   
async def gexp(ctx, user: discord.User, arg):
	expf = open('rpb/players/' + user.name + '/exp.txt')
	exp = int(expf.read())
	expf.close()
	exp = exp + int(arg)
	lvlf = open('rpb/players/' + user.name + '/lvl.txt')
	lvl = int(lvlf.read())
	lvlf.close()
	if exp + 1 > 100 + int(lvl) * 20:
		succ = '0'
		while succ != '1':
			expg = 100 + int(lvl) * 20
			exp = exp - expg
			lvl = int(lvl) + 1
			if exp + 1 > 100 + int(lvl) * 20:
				succ = '0'
			else:
				succ = '1'
		hpf = open('rpb/players/' + user.name + '/hp.txt')
		hp = int(hpf.read())
		hpf.close()
		hp = hp + 30
		hpf = open('rpb/players/' + user.name + '/hp.txt', 'w')
		hpf.write(str(hp))
		hpf.close()
		await ctx.send('Игрок ' + user.name + ' получил ' + str(arg) + ' опыта и новый уровень. Теперь у него ' + str(lvl) + ' лвл. +30 хп.')
	else:
		await ctx.send('Игрок ' + user.name + ' получил ' + str(arg) + ' опыта, теперь у него ' + str(exp) + ' опыта.')	
	expf = open('rpb/players/' + user.name + '/exp.txt', 'w')
	expf.write(str(exp))
	expf.close()
	lvlf = open('rpb/players/' + user.name + '/lvl.txt', 'w')
	lvlf.write(str(lvl))
	lvlf.close()

@bot.command(pass_context=True)   
async def smoney(ctx, user: discord.User, arg):
	mof = open('rpb/players/' + user.name + '/money.txt')
	mo = int(mof.read())
	mof.close()
	if int(arg) > int(mo):
		await ctx.send('Ошибка, у игрока ' + user.name + ' не хватает ' + str(int(arg) - int(mo)) + ' монет ' + format(ctx.message.author.mention))
	else:
		mo = mo - int(arg)
		await ctx.send('Игрок ' + user.name + ' потратил ' + str(arg) + ' монет, теперь у него ' + str(mo) + ' монет.')
		mof = open('rpb/players/' + user.name + '/money.txt', 'w')
		mof.write(str(mo))
		mof.close()

@bot.command(pass_context=True)   
async def stat(ctx, user: discord.User):
	mof = open('rpb/players/' + user.name + '/money.txt')
	mo = int(mof.read())
	mof.close()
	hpf = open('rpb/players/' + user.name + '/hp.txt')
	hp = int(hpf.read())
	hpf.close()
	expf = open('rpb/players/' + user.name + '/exp.txt')
	exp = int(expf.read())
	expf.close()
	lvlf = open('rpb/players/' + user.name + '/lvl.txt')
	lvl = int(lvlf.read())
	lvlf.close()
	await ctx.send('У игрока ' + user.name + ': \n- ' + str(mo) + ' монет\n- ' + str(hp) + ' хп\n- ' + str(lvl) + ' уровень\n- ' + str(exp) + ' опыта')

@bot.command(pass_context=True)   
async def pay(ctx, user1: discord.User, user2: discord.User, arg):
	mo1f = open('rpb/players/' + user1.name + '/money.txt')
	mo1 = int(mo1f.read())
	mo1f.close()
	mo2f = open('rpb/players/' + user2.name + '/money.txt')
	mo2 = int(mo2f.read())
	mo2f.close()
	if int(arg) > int(mo1):
		await ctx.send('Ошибка, у игрока ' + user1.name + ' не хватает ' + str(int(arg) - int(mo1)) + ' монет ' + format(ctx.message.author.mention))
	else:
		mo1 = mo1 - int(arg)
		mo1f = open('rpb/players/' + user1.name + '/money.txt', 'w')
		mo1f.write(str(mo1))
		mo1f.close()
		mo2 = mo2 + int(arg)
		mo2f = open('rpb/players/' + user2.name + '/money.txt', 'w')
		mo2f.write(str(mo2))
		mo2f.close()
		await ctx.send('Игрок ' + user1.name + ' передал игроку ' + user2.name + ' ' + str(arg) + ' монет, теперь у игрока ' + user2.name + ' ' + str(mo2) + ' монет.')

bot.run("NjU3OTg3NzA3NTQwMzQwNzkx.Xf5NDQ.PflQ0TZ4iKUzisVebHQljb6asS8")
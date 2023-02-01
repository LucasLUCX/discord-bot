import requests
import discord
from discord.ext import commands
from discord import app_commands
import random

bot = commands.Bot(command_prefix = '.',intents = discord.Intents.all(),help_command = None)

@bot.event
async def on_ready():
	await bot.change_presence(status = discord.Status.dnd,activity= discord.Streaming(name ='.help', url = "https://www.youtube.com/watch?v=AY5evVWEC4Q" ,platform = "YouTube",game = "Femboy hooters") )
	print('im online')

@bot.command()
async def help(ctx):
	embed = discord.Embed(title = 'commands', description = 'all commands that i have',colour = discord.Colour.random())
	embed.add_field(name = 'Coinflip',value = 'rng between head/number')                     #done
	embed.add_field(name = 'Dog',value = 'send random picture of Dog',inline = False)         #done
	embed.add_field(name = 'Fox',value = 'send random picture of Fox',inline = False)         #done
	embed.add_field(name = 'Coffe',value = 'send random picture of Coffe',inline = False)    #done
	embed.add_field(name = 'Femboy',value = 'send random picture of Femboy',inline = False)         #done
	embed.add_field(name = 'Truth',value = 'give random question for you to answer',inline = False)   #done
	embed.add_field(name = 'Say',value = 'will repeat something you say',inline = False)                  #done
	embed.add_field(name = '8ball',value = 'will give you random anser to your question',inline = False)  # 	done
	embed.add_field(name = 'Dice',value = 'random number from 1-6 ',inline = False)                       #done
	embed.add_field(name = 'Femres',value = 'random femboy answer ',inline = False)                    #done
	embed.add_field(name = 'kick',value = 'kick user ',inline = False)                    #done
	embed.add_field(name = 'ban',value = 'ban user ',inline = False)                    #done
	await ctx.reply(embed = embed)

#---------------------------------------
#/will genrate random number bettween  /
#/1-2 if 1 head else 2                 /
#---------------------------------------
@bot.command(aliases=['Coinflip'])
async def coinflip(ctx):
	if random.randint(1,2) == 1: await ctx.send('head')
	else: await ctx.send('number')

#--------------------------------------------------------------
#/will grab a pcture of dog which is grabbed from an api in r /
#--------------------------------------------------------------
@bot.command(aliases=['Dog'])
async def dog(ctx):
	r = requests.get("https://dog.ceo/api/breeds/image/random")
	res = r.json()
	em = discord.Embed() 
	em = discord.Embed(colour = discord.Colour.random())
	em.set_image(url=res['message'])
	await ctx.send(embed = em)

#--------------------------------------------------------------
#/will grab a pcture of fox which is grabbed from an api in r /
#--------------------------------------------------------------
@bot.command(aliases=['Fox'])
async def fox(ctx):
	r = requests.get("https://randomfox.ca/floof/")
	res = r.json()
	em = discord.Embed() 
	em = discord.Embed(colour = discord.Colour.random())
	em.set_image(url=res['image'])
	await ctx.send(embed = em)

#----------------------------------------------------------------
#/will grab a pcture of coffe which is grabbed from an api in r /
#----------------------------------------------------------------
@bot.command(alliases=['Coffe'])
async def coffe(ctx):
	r = requests.get('https://coffee.alexflipnote.dev/random.json')
	res = r.json()
	em = discord.Embed()
	em = discord.Embed(colour = discord.Colour.random())
	em.set_image(url = res['file'])
	await ctx.send(embed = em)

#-----------------------------------------------------------------
#/will grab a pcture of catboy which is grabbed from an api in r /
#-----------------------------------------------------------------
@bot.command(aliases=['Femboy'])
async def femboy(ctx):
	r = requests.get("https://api.catboys.com/img")
	res = r.json()
	em = discord.Embed() 
	em = discord.Embed(colour = discord.Colour.random())
	em.add_field(name = "artist name: " + res['artist'],value = 'art url: ' + res["artist_url"],inline = False)
	em.set_image(url=res['url'])
	await ctx.send(embed = em)

#-----------------------------------------
#/will grab a random text from an an api /
#-----------------------------------------
@bot.command(aliases=['Truth'])
async def truth(ctx):
	r = requests.get("https://api.truthordarebot.xyz/v1/truth")
	res = r.json()
	await ctx.send(res['question'])

#------------------------------------
#/just repost of what the user says /
#------------------------------------
@bot.command(aliases = ['Say'])
async def say(ctx,*,con):
	await ctx.send(con)

#-----------------------------------------
#/will grab a random text from an an api /
#-----------------------------------------
@bot.command(alliases = ['8Ball','8b',"8B"])
async def ball(ctx,*,con):
	r = requests.get("https://api.catboys.com/8ball")
	res = r.json()
	await ctx.send(f'question: {con} / answer: ' + res['response'])

#--------------------------------
#/randomli generates number 1-6 /
#--------------------------------
@bot.command(aliases = ['Dice'])
async def dice(ctx):
	await ctx.send(random.randint(1,6))

#-----------------------------------------
#/will grab a random text from an an api /
#-----------------------------------------
@bot.command(aliases = ['Femres'])
async def femres(ctx,*,con):
	r = requests.get("https://api.catboys.com/catboy")
	res = r.json()
	await ctx.reply(res['response'])

#---------------------------------------------
#/will kick a memeber if user has permission /
#---------------------------------------------
@bot.command(aliases = ['Kick'])
@commands.has_permissions(kick_member = True)
async def kick(ctx, member:discord.Member,*,reason = None):
	if reason == None:
		reason = 'no reason provided'
	await ctx.guild.kick(member)
		await ctx.send(f'{member.mention} has been kicked for {reason}')

#--------------------------------------------
#/will  a mbanemeber if user has permission /
#--------------------------------------------
@bot.command(aliases = ['Ban'])
@commands.has_permissions(ban_member = True)
async def ban(ctx, member:discord.Member,*,reason = None):
	if reason == None:
		reason = 'no reason provided'
	await ctx.guild.ban(member)
		await ctx.send(f'{member.mention} has been ban for {reason}')

bot.run("your-token-goes-here")
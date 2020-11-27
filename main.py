from bs4 import BeautifulSoup
from requests_html import HTMLSession
from webdriver import keep_alive
import discord

from discord.ext import commands

bot = commands.Bot(command_prefix='!')
bot.remove_command("help")

@bot.event
async def on_ready():
	await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=""))
	print(f'Logged in as {bot.user.name}')

@commands.command(name="fees")
async def fees(ctx, arg):
	inp = int(arg)
	ebay = inp * 0.90
	amazon = inp * 0.85

	await ctx.send("Amazon: $" + str(amazon))
	await ctx.send("Ebay: $" + str(ebay))



bot.add_command(fees)


keep_alive()

bot.run('')


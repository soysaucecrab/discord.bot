import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot
import os

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('안녕하세요?')

@bot.command()
async def 쿠코(ctx):
    await ctx.send('반가워요')

@bot.command()
async def 섭주(ctx):
    await ctx.send('soysaucecrab.kro.kr')

@bot.command()
async def 서버주소(ctx):
    await ctx.send('soysaucecrab.kro.kr')

    
access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)

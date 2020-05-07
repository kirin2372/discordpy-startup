from discord.ext import commands
import os
import traceback
import discord

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
TOKEN = 'NzA1MzY4NzQ2NTAzNDM4Mzg2.XrOkwQ.wWpdZ6soWRVukKLBgaO8KxcsxTU'


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

client = discord.Client()
@client.event
async def on_message(message):
    if message.author.bot:
        return
     if message.content == '/neko':
        await message.channel.send('にゃーん')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)

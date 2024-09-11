# This bot requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import subprocess

description = '''A bot that lets admins run basic minecraft commands such as whitelist from Discord. Made for the itzg/minecraft docker image.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

base_command = "sudo docker exec minecraft-server-mc-1 rcon-cli"

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.listen()
async def on_message(message):
    if message.author.bot:
        return

@bot.command()
async def ping(ctx):
    """Ping!"""
    await ctx.reply("Pong")

@bot.command()
@commands.has_permissions(administrator = True)
async def whitelist(ctx, option: str, user: str):
    """Adds or removes a user to the whitelist."""
    if option not in ['add', 'remove']:
        return
    else:
     command = subprocess.check_output(f"{base_command} whitelist {option} {user}", shell=True, text=True)
     await ctx.reply(command)

@bot.command()
@commands.has_permissions(administrator = True)
async def op(ctx, user: str):
    """Ops a user."""
    command = subprocess.check_output(f"{base_command} op {user}", shell=True, text=True)
    await ctx.reply(command)

@bot.command()
@commands.has_permissions(administrator = True)
async def deop(ctx, user: str):
    """Ops a user."""
    command = subprocess.check_output(f"{base_command} deop {user}", shell=True, text=True)
    await ctx.reply(command)

@bot.command()
async def list(ctx):
    """Lists online players"""
    command = subprocess.check_output(f"{base_command} list", shell=True, text=True)
    await ctx.reply(command)

bot.run('TOKEN')

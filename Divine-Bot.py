import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import os
import random
from itertools import cycle


Client = discord.Client()
bot = commands.Bot(command_prefix='!!')
bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="with commands!"))
    print ("Ready when you are.")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def Ping(ctx):
    await bot.say(":ping_pong: Pong!!")
    print ("user has pinged.")

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: Pong!!")
    print ("user has pinged.")

@bot.command(pass_context=True)
async def Pong(ctx):
    await bot.say(":ping_pong: Ping!!")
    print ("user has ponged.")

@bot.command(pass_context=True)
async def pong(ctx):
    await bot.say(":ping_pong: Ping!!")
    print ("user has ponged.")

@bot.command(pass_context=True)
async def Info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0xFFFB00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0xFFFB00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_role("DIVINES")
async def Kick(ctx, user: discord.Member):
    await bot.say("I do apollogize, its just orders {}.".format(user.name))
    await bot.kick(user)
    print ("{} has been kicked.".format(user.name))

@bot.command(pass_context=True)
@commands.has_role("DIVINES")
async def kick(ctx, user: discord.Member):
    await bot.say("I do apollogize, its just orders {}.".format(user.name))
    await bot.kick(user)
    print ("{} has been kicked.".format(user.name))

@bot.command(pass_context=True)
@commands.has_role("DIVINES")
async def Ban(ctx, user: discord.Member):
    await bot.say("Sorry but you have been let go {}.".format(user.name))
    await bot.ban(user)
    print ("{} has been banned.".format(user.name))

@bot.command(pass_context=True)
@commands.has_role("DIVINES")
async def ban(ctx, user: discord.Member):
    await bot.say("Sorry but you have been let go {}.".format(user.name))
    await bot.ban(user)
    print ("{} has been banned.".format(user.name))

@bot.command(pass_context=True)
@commands.has_role("DIVINES")
async def Unban(ctx, user: discord.Member):
    await bot.say("Welcome back {}!".format(user.name))
    await bot.unban
    print ("{} has been unbanned.".format(user.name))

@bot.command(pass_context=True)
@commands.has_role("DIVINES")
async def unban(ctx, user: discord.Member):
    await bot.say("Welcome back {}!".format(user.name))
    await bot.unban
    print ("{} has been unbanned.".format(user.name))

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Server information")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def Serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Server information")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ServerInfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Server information")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_role("DIVINES")
async def Clear(ctx, amount=10):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await bot.delete_messages(messages)
    await bot.say("Messages deleted.")
    print ("Messages deleted in {}".format(ctx.message.channel))
    
@bot.command(pass_context=True)
@commands.has_role("DIVINES")
async def clear(ctx, amount=10):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await bot.delete_messages(messages)
    await bot.say("Messages deleted.")
    print ("Messages deleted in {}".format(ctx.message.channel))

@bot.command(pass_context=True)
async def Help(ctx):
    author = ctx.message.author
    embed = discord.Embed(title="Commands", description=" .Ping .Pong .Info [User] .Serverinfo", color=0x00ff00)
    embed.set_author(name="Help")
    await bot.send_message(author, embed=embed)

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(title="Commands", description=" .Ping .Pong .Info [User] .Serverinfo", color=0x00ff00)
    embed.set_author(name="Help")
    await bot.send_message(author, embed=embed)

@bot.command(pass_context=True)
@commands.has_role("DIVINES")
async def Admin_Help(ctx):
    author = ctx.message.author
    embed = discord.Embed(title="Commands", description=" .Kick .Ban .Unban .Ping .Pong .Info [User] .Serverinfo", color=0x00ff00)
    embed.set_author(name="Help")
    await bot.send_message(author, embed=embed)

@bot.command(pass_context=True)
@commands.has_role("DIVINES")
async def Admin_help(ctx):
    author = ctx.message.author
    embed = discord.Embed(title="Commands", description=" .Kick .Ban .Unban .Ping .Pong .Info [User] .Serverinfo", color=0x00ff00)
    embed.set_author(name="Help")
    await bot.send_message(author, embed=embed)

@bot.command(pass_context=True)
@commands.has_role("DIVINES")
async def admin_help(ctx):
    author = ctx.message.author
    embed = discord.Embed(title="Commands", description=" .Kick .Ban .Unban .Ping .Pong .Info [User] .Serverinfo", color=0x00ff00)
    embed.set_author(name="Help")
    await bot.send_message(author, embed=embed)

@bot.command(pass_context=True)
@commands.has_role("DIVINES")
async def Help_Admin(ctx):
    author = ctx.message.author
    embed = discord.Embed(title="Commands", description=" .Kick .Ban .Unban .Ping .Pong .Info [User] .Serverinfo", color=0x00ff00)
    embed.set_author(name="Help")
    await bot.send_message(author, embed=embed)

@bot.command(pass_context=True)
@commands.has_role("DIVINES")
async def Help_admin(ctx):
    author = ctx.message.author
    embed = discord.Embed(title="Commands", description=" .Kick .Ban .Unban .Ping .Pong .Info [User] .Serverinfo", color=0x00ff00)
    embed.set_author(name="Help")
    await bot.send_message(author, embed=embed)

@bot.command(pass_context=True)
@commands.has_role("DIVINES")
async def help_admin(ctx):
    author = ctx.message.author
    embed = discord.Embed(title="Commands", description=" .Kick .Ban .Unban .Ping .Pong .Info [User] .Serverinfo", color=0x00ff00)
    embed.set_author(name="Help")
    await bot.send_message(author, embed=embed)

bot.run(os.getenv('TOKEN'))

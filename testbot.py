import asyncio
import discord
from discord import member
from discord.ext import  commands 
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument

#need to add Verification , command roles and announcements for today , excessive chat spammer bot.
#next day have to add exceptions on role missing
#command.has_role is also a thing which can be used for future
bot = commands.Bot(command_prefix='>>' , help_command = None)

@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.idle, activity=discord.Game(" with ur mom."))
    print("We are ready to go!")

@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server')#usage of F strings
    role = discord.utils.get(member.server.roles , name = "Beta role rofl")
    await bot.add_roles(member , role)
@bot.event 
async def on_member_leave(member):
    print(f"{member} has left the server")

@bot.event
async def on_command_error(ctx, error):# general error for command not found
    if isinstance(error,CommandNotFound):
        await ctx.send("Command does not exist. >>help to check list of commands and their syntax.")



@bot.command(name = "ping")# test command
async def ping(obj):
    embed = discord.Embed(title = "Ping", description ="Check the latency of the bot" , color = 0x006400)
    embed.add_field(name = "Latency - " , value = int(bot.latency*1000) , inline = False)
    embed.set_thumbnail(url ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTTbUZC7rVkyHQ8S7IdAuSE7uxrS7aj0awYw&usqp=CAU")
    #await obj.send(f"ping --> {int(bot.latency*1000)} ms") 
    await obj.channel.send(embed = embed)
    
@bot.command(name = 'purge')#deletes num number of messages
@commands.has_permissions(manage_messages=True)
async def purge(ctx, num:int):
    embed = discord.Embed(title="Message Deleted", description =f"{num} messages have been deleted from the channel.", color = 0x006400)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/811305082377207866/882970862221918238/unknown.png?width=400&height=248")
    await ctx.channel.purge(limit=num)
    await ctx.channel.send(embed = embed)


@bot.command(name = 'kick')
@commands.has_permissions(kick_members= True)
async def kick(ctx , usr:discord.Member, * , reason=None):# bydefault ifnothing is specified it will give no reason
    await usr.kick(reason = reason)
    embed = discord.Embed(title = "Kick" , description =f"{usr.mention} has been kicked. " , color = 0x006400)
    embed.add_field(name="Reason" , value = reason , inline = False)
    embed.set_thumbnail(url = 
    "https://www.clipartmax.com/png/middle/185-1855950_28-collection-of-boot-kicking-clipart-high-quality-kicking-boot-clip-art.png")
   # await ctx.send(f"Kicked {usr.mention}")
    await  ctx.send(embed = embed)

@bot.command(name='char')
async def char(ctx , *,name:str):
    embed = discord.Embed(title = "Charpage" , description ="Click on the link below to check his/her charpage" , color = 0x006400 )
   # await ctx.send("https://account.aq.com/CharPage?id="+name)
    embed.add_field(name="Username" , value = f"{name}" , inline = False)
    name=name.replace(" ", "%20")
    embed.add_field(name="AQW CharPage - " ,value = f"https://account.aq.com/CharPage?id={name}" , inline = False)
    embed.set_thumbnail(url = "https://www.aq.com/shared/launcher/img/aqw-logo-lg.png")
    await ctx.send(embed = embed)


@bot.command(name='membership')
async def membership(ctx):
    embed = discord.Embed(title = "AQW Membership" , description = "Click the link below to buy Upgrade packages/ACs." , color = 0x006400)
    embed.add_field(name="Link - " , value = "https://www.aq.com/order-now/direct/")
    embed.set_thumbnail(url = "https://www.aq.com/shared/launcher/img/aqw-logo-lg.png")
    await ctx.send(embed = embed)


@bot.command(name='accountAQW')
async def account(ctx):
    embed = discord.Embed(title = "AQW Account Manager" , description = "Click the link below to Access account manager." , color = 0x006400)
    embed.add_field(name="Link - " , value = "https://account.aq.com/login")
    embed.set_thumbnail(url = "https://www.aq.com/shared/launcher/img/aqw-logo-lg.png")
    await ctx.send(embed = embed)


@bot.command(name = 'ban')
@commands.has_permissions(ban_members=True)
async def ban(ctx , usr:discord.Member, * , reason=None):# bydefault ifnothing is specified it will give no reason
    await usr.ban(reason = reason)
    embed = discord.Embed(title="Ban", description =f"User {usr.mention} has been banned from the server.", color = 0x006400)
    embed.add_field(name="Reason -" , value= reason , inline = False)
    embed.set_thumbnail(url = "https://cdn.siasat.com/wp-content/uploads/2019/10/Banned.jpg")
    #await ctx.send(f"Banned {usr.mention}")
    await ctx.send(embed = embed)

@bot.command(name = "tempmute")#need to have a "Muted" role to make this work
@commands.has_role("chat moderator")# need to have a role called chat moderator to use this command
async def tempmute(ctx,usr:discord.Member,time:int,*, reason=None):
    t = time# in mins
    rolex = discord.utils.get(ctx.guild.roles, name="Muted")
    await usr.add_roles(rolex)
    embed = discord.Embed(title="Mute" , description=f"User {usr.mention} has been muted for {t} min" , color = 0x006400)
    embed.add_field(name = "Reason" , value = reason)
    embed.set_thumbnail(url="https://ih1.redbubble.net/image.44036746.0268/flat,750x1000,075,f.u2.jpg")
    await ctx.send(embed = embed)
    await asyncio.sleep(t*60)
    await usr.remove_roles(rolex)
    await ctx.send(f"Your mute is over {usr.mention}")



@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title = "Help", description = "Shows a list of commands along with their arguments." , 
    color = 0x006400)
    embed.set_author(name = "Not Alina" , url = "https://aq.com" , icon_url="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_960_720.jpg")
    embed.set_footer(text = "Made by Wh0_")
    embed.add_field(name="ping" , value = "Pings the bot to check latency, >>ping" , inline = False)
    embed.add_field(name="purge" , value = "Deletes number of lines specified (Needs permission), >>purge <no of lines>" , inline = False)
    embed.add_field(name="kick" , value = "Kicks an user (Needs permission), >>kick <user>" , inline = False)
    embed.add_field(name="ban" , value = "Bans an user (Needs permission), >>ban <user>" , inline = False)
    embed.add_field(name="char" , value = "Gives the link for the charpage of a user, >>char <username in aqw>" , inline = False)
    embed.add_field(name="tempmute" , value = "Mutes a user for a specified time , >>tempmute <user> <time in mins> <reason>" , inline = False)
    embed.add_field(name="accountAQW" , value = "Account Manager AQW , >>accountAQW " , inline = False)
    embed.add_field(name="membership" , value = "Membership page for aqw , >>membership" , inline = False)
    embed.set_thumbnail(url=
    "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/cd3b1023-a009-4c0e-a47b-033bcea6c840/dah479y-eb9c07ee-4ef7-4c41-8386-6274211f40d3.png/v1/fill/w_1182,h_676,strp/gravelyn_nude_2_by_dartguy86_dah479y-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTE3MiIsInBhdGgiOiJcL2ZcL2NkM2IxMDIzLWEwMDktNGMwZS1hNDdiLTAzM2JjZWE2Yzg0MFwvZGFoNDc5eS1lYjljMDdlZS00ZWY3LTRjNDEtODM4Ni02Mjc0MjExZjQwZDMucG5nIiwid2lkdGgiOiI8PTIwNDkifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.IOa-_MVJwBOFzCjsyuMHxwqblSjjvt6NPgimhSkHTl0")

    await ctx.send(embed = embed)



@bot.command(name = "testDM")#this is a beta function still in test
async def dm(ctx):
    usr = ctx.message.author
    message = "this is just a test message"                                             
    await usr.send(message)


@purge.error
async def purge_error(ctx, error):
    if isinstance(error , MissingRequiredArgument):# need to make more number of errors
        await ctx.send("Missing arguments (No. of messages to delete) , >>help to check list of commands and their syntax.")

@char.error
async def purge_error(ctx, error):
    if isinstance(error , MissingRequiredArgument):# need to make more number of errors
        await ctx.send("Specify the name of the User you want to CharPage, >>help to check list of commands and their syntax.")

@kick.error
async def purge_error(ctx, error):
    if isinstance(error , MissingRequiredArgument):# need to make more number of errors
        await ctx.send("Missing arguments (Specify/Tag the user u want to kick ,>>help to check list of commands and their syntax.)")

@ban.error
async def purge_error(ctx, error):
    if isinstance(error , MissingRequiredArgument):# need to make more number of errors
        await ctx.send("Specify the name of the User you want to Ban, >>help to check list of commands and their syntax.")

@tempmute.error
async def purge_error(ctx, error):
    if isinstance(error , MissingRequiredArgument):# need to make more number of errors
        await ctx.send("Missing arguments (User and/or time , >>help to check list of commands and their syntax.)")



bot.run('SOME_BOT_TOKEN')

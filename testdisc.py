import discord
from discord.ext.commands.errors import CommandInvokeError, MissingRequiredArgument, MissingRole
import pymongo
from discord.ext import commands
from decoder1 import decode_username

bot = commands.Bot(command_prefix = ">>" , intentions = discord.Intents.all())
client = pymongo.MongoClient("mongodb+srv://testusr:testusr@cluster0.xrzw0.mongodb.net/testDB?retryWrites=true&w=majority")
db = client.testDB
#make all inputs to lowercase ffs rofl 

@bot.event
async def on_ready():
    print("we are ready!")


@bot.command(name = "add_usr")#needs role ingame verified to make it work
async def add_usr(ctx ,*,usr:str):
    c = db["username"]
    usr = usr.lower()
    disc_usr = ctx.author
    id = str(ctx.author.id)
    c.insert_one({"_id":f"{id}" ,  "username":f"{usr}"})
    await ctx.send("`Discord user Registered in database.`")
    role  = discord.utils.get(ctx.guild.roles , name = "Ingame Verified")
    role2 = discord.utils.get(ctx.guild.roles , name ="Guild member")
    c2 = db["guild"]
    c2_data = c2.find_one({"name":f"{usr}"})
    if (c2_data != None):
        await disc_usr.add_roles(role2)
        await ctx.send("**Welcome Guild Member , enjoy ur stay!**")
    else:
        #print("Not a guild member!")
        await ctx.send("**Welcome , enjoy ur stay!**")
    
    await  disc_usr.add_roles(role)



@bot.command(name ="check_usr")
async def check_usr(ctx,usr:discord.Member):
    id = usr.id
    c = db["username"]
    data =  c.find_one({"_id":f"{id}"})
    if (data != None):
        decoded_data = decode_username(str(data))
        decoded_data = decoded_data.replace("username:" , "--->")
        decoded_data = f"`{decoded_data}`"
        await ctx.send(str(decoded_data))
    else:
        await ctx.send("No AQW User found for this Discord user.")


@bot.command(name = "add_gmember")
@commands.has_role("Officer")
async def add_gmember(ctx,*,usr:str):
    usr = usr.lower()
    c = db["guild"]
    if (c.find_one({"name":f"{usr}"})==None): 
        c.insert_one({"name":f"{usr}"})
        await ctx.send(f"`Added User {usr} in Guild Member database.`")
    else: 
        await ctx.send("`User already present in Guild Member database.`")

@bot.command(name= "guild_show")
async def guild_show(ctx):
    c = db["guild"]
    all_data  = c.find()
    out  = ""
    for data in all_data:
        decoded_data = decode_username(str(data))
        decoded_data = decoded_data.replace("name:","")
        out = out +"\n"+decoded_data
    out = f"```{out}```"
    await ctx.send(out)

@bot.command(name = "remove_gmember")
@commands.has_role("Officer")
async def remove_gmember(ctx , usr:str):
    usr = usr.lower()
    c = db["guild"]
    if(c.find_one({"name":f"{usr}"})!=None):
        c.delete_one({"name":f"{usr}"})
        await ctx.send(f"`Deleted user {usr} from Guild Members.`")
    else:
        await ctx.send("`User Not found in database.`")



@add_usr.error
async def on_add_usr_error(ctx, error):
    if isinstance(error , CommandInvokeError):
       await ctx.send("Discord User already present in database.")
    if isinstance(error , MissingRequiredArgument):
        await ctx.send("Argument is missing, use >>help.")


@check_usr.error
async def on_add_usr_error(ctx, error):
    if isinstance(error , MissingRequiredArgument):
        await ctx.send("Argument missing use >>help.")


@add_gmember.error
async def on_add_usr_error(ctx, error):
    if isinstance(error , MissingRequiredArgument):
        await ctx.send("Argument missing use >>help.")
    if isinstance(error ,MissingRole):
        await ctx.send("Required role is missing , use >>help")


@remove_gmember.error
async def on_add_usr_error(ctx, error):#name wont make a diff cuz its taken as formal parameter
    if isinstance(error , MissingRequiredArgument):
        await ctx.send("Argument missing use >>help.")
    if isinstance(error ,MissingRole):
        await ctx.send("Required role is missing , use >>help")


bot.run("token")

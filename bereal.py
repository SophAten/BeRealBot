#insult my code and ill cry
import discord, os, datetime, asyncio, random, pytz
from discord.ext import commands
from datetime import time
from dotenv import load_dotenv

load_dotenv()

MST = pytz.timezone('America/Phoenix')
intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

global dt
global dateformat
dt = datetime.datetime.now()
dateformat = dt.strftime('%x')


async def createThread():
    

    channel = bot.get_channel(1068374707218427966)
    global thread
    thread = await channel.create_thread(
        name= (dateformat),
        type= discord.ChannelType.private_thread,
        invitable=False
    )
    embed = discord.Embed(title="BeReal of {}".format(dateformat), description= ":warning: It's Time To Be Real! :warning:", color= 2303786)
    embed.set_author(name="BeFuckingForRealBot", icon_url="https://upload.wikimedia.org/wikipedia/en/4/40/BeReal_logo.png")
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/en/4/40/BeReal_logo.png")
    await thread.send(embed=embed)
    return thread

#when this command is disabled it gives you an error message when someone uses it
# and idk how to change that, the error msg doesnt rlly mean anythin tho 
#cuz i want it to be disabled i tried doing it with the error() function but it doesnt work.
@bot.command()
async def submit(ctx):

    member = ctx.author

     
    if len(ctx.message.attachments) == 2:
        await thread.send("{} Was Being Fucking For Real Today!".format(ctx.message.author.mention))
        name = member.display_name
        pfp = member.display_avatar
                
        embed = discord.Embed(title = "{}'s BeReal".format(name), color=discord.Color.random(), timestamp=ctx.message.created_at)
        embed.set_author(name=f"{name}", icon_url=f"{pfp}")
                
        url1 = ctx.message.attachments[0].url
        embed.set_thumbnail(url=(url1))
        url2 = ctx.message.attachments[1].url
        embed.set_image(url=(url2))
        await thread.send(embed=embed)
    else:
        await ctx.send("Please submit 2 images!!!")

global command
command = bot.get_command('submit')
command.update(enabled=False)

async def BeRealNotif():
    while True:
        now = datetime.datetime.now(MST)
        print(now)

        h = random.randint(0, 23)
        m  = random.randint (0, 59)
        s = random.randint(0, 59)

        then = now.replace(hour=h, minute = m, second= s)
        then += datetime.timedelta(days=1)
        print(h)
        print(m)
        print(s)

        wait_time=(then-now).total_seconds()
        await asyncio.sleep(wait_time)

        
        channel = bot.get_channel(1068374707218427966)
        role = "<@&1068375452885987370>"

        await channel.send(role + " :warning: It's time to be fucking for real! You have 10 minutes to DM me 2 images :warning: DM me `.submit` with 2 images. The first image is the front camera, the second is the back.")
        await itsTime()

@bot.command()
async def bereal(ctx):

    channel = bot.get_channel(1068374707218427966)
    role = "<@&1068375452885987370>"

    await channel.send(role + " :warning: It's time to be fucking for real! You have 3 minutes to DM me 2 images :warning: ")
    await itsTime()

    await BeRealNotif()

async def itsTime():
    timenow = datetime.datetime.now(MST)
    timelimit = timenow + datetime.timedelta(minutes=10)
    command.update(enabled=True)
    await createThread()
    wait2_time = (timelimit-timenow).total_seconds()
    await asyncio.sleep(wait2_time)
    command.update(enabled=False)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
   # error()

# u gotta replace this with ur botty bot key or sum
bot.run(os.getenv('DISCORD_TOKEN', default=''))
#insult my code and ill cry
import discord, os, datetime, asyncio, random, pytz
from discord.ext import commands
from datetime import time
from dotenv import load_dotenv

load_dotenv()

MST = pytz.timezone('America/Phoenix')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)
bot.thread = None
bot.count = 0

message = "<@&1068375452885987370> :warning: It's time to be real! You have 10 minutes to DM me 2 images :warning: DM me `.submit` with 2 images. The first image is the front camera, the second is the back."

async def createThread():
    dt = datetime.datetime.now(MST)
    dateformat = dt.strftime('%x')
    if bot.thread:
        await bot.thread.edit(archived=True, locked=True)
    channel = bot.get_channel(1068374707218427966)
    thread = await channel.create_thread(
        name= (dateformat),
        type= discord.ChannelType.private_thread,
        invitable=False
      )
    embed = discord.Embed(title="BeReal of {}".format(dateformat), description= ":warning: It's Time To Be Real! :warning:", color= 2303786)
    embed.set_author(name="BeRealBot", icon_url="https://upload.wikimedia.org/wikipedia/en/4/40/BeReal_logo.png")
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/en/4/40/BeReal_logo.png")
    await thread.send(embed=embed)
    bot.thread = thread
    bot.count = 0

@bot.command()
async def submit(ctx):
    member = ctx.author
    thread = ctx.bot.thread
     
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
        bot.count += 1
    else:
        await ctx.send("Please submit 2 images!!!")

async def BeRealNotif():
    while True:
        now = datetime.datetime.now(MST)

        h = random.randint(8, 23)
        m  = random.randint (0, 59)
        s = random.randint(0, 59)
        print(f'{h} {m} {s}')

        then = now.replace(hour=h, minute = m, second= s) + datetime.timedelta(days=1)
        print(f'{then!r}')

        await asyncio.sleep((then-now).total_seconds())

        await notify()

async def notify(current_thread):
    channel = bot.get_channel(1068374707218427966)
    msg = await channel.send(message)

    command.update(enabled=True)
    await createThread()
    wait2_time = datetime.timedelta(minutes=10).total_seconds()
    await asyncio.sleep(wait2_time)
    command.update(enabled=False)
    await msg.edit(content=f"Time's up losers. Number of people that were real today: {bot.count}")

@bot.command()
@commands.has_permissions(administrator=True)
async def bereal(ctx):
    await notify(None)
    await BeRealNotif()

    
@bereal.error
async def bereal_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"You need {error.missing_perms} permissions to use this command.")
        

global command
command = bot.get_command('submit')
command.update(enabled=False)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# u gotta replace this with ur botty bot key or sum
bot.run(os.getenv('DISCORD_TOKEN', default=''))

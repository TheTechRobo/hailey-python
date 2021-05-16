from discord.ext import commands
import discord, sys, asyncio, configparser, logging, random

logging.basicConfig(level=logging.INFO, format='%(levelname)s @ %(asctime)s: %(message)s; Lineno %(lineno)d, func %(funcName)s, file %(filename)s.', datefmt='%d/%m/%Y %H:%M:%S')

try:
    from hailey_data.INFO import PREFIX, VERSION, welcomeMessage, leaveMessage, DISCORD_MEMBER_INTENT
except Exception:
    print("Failed to load configuration. Make sure that a `hailey_data' folder exists, with a file called INFO.py inside with the correct configuration.\nA full traceback is below:\n\n")
    raise
try:
    with open("TOKEN.txt") as file:
        TOKEN = file.read()
except Exception:
    print("FAILED TO LOAD TOKEN.\nPlease put a file called TOKEN.txt inside this folder, containing solely the token.")
    sys.exit(8)
logging.info(f"Token in use: {TOKEN}")

if DISCORD_MEMBER_INTENT is True:
    intents = discord.Intents.default()
    intents.members = True
    bot = commands.Bot(command_prefix=PREFIX, intents=intents)
else:
    logging.warn("*** Intents disabled. Join/leave messages are disabled.")
    bot = commands.Bot(command_prefix=PREFIX)

for extension in ("moderation", "roles"):
    extension = f"hailey_data.{extension}"
    bot.load_extension(extension)
    logging.info(f"LOADED EXTENTION {extension}")

@bot.event
async def on_ready():
    print("Ready for action Rider sir!")
    final = ""
    for word in "Paw Patrol!!! Paw Patrol!!!! We'll be there on the double!!!!!!!!!!!!":
        for character in word:
            uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1\\"
            lowercase = "abcdefghijklmnopqrstuvwxyz!'"
            if character in lowercase:
                if random.randint(0,2) == 1:
                    final += character
                    continue
                pos = lowercase.find(character)
                final += uppercase[pos]
            elif character in uppercase:
                if random.randint(0,2) == 1:
                    final += character
                    continue
                pos = uppercase.find(character)
                final += lowercase[pos]
            else:
                final += character
        final += " "
    final += "!"
    print(final)
if DISCORD_MEMBER_INTENT is True:
    @bot.event
    async def on_member_join(ctx):
        await ctx.send(welcomeMessage)
    @bot.event
    async def on_member_remove(ctx):
        await ctx.send(leaveMessage) #ONLY sends if user is in another server with the SAME INSTANCE of the bot running

bot.run(TOKEN)

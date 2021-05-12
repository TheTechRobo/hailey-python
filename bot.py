from discord.ext import commands
import discord, sys, asyncio, configparser, logging, random

logging.basicConfig(level=logging.INFO, format='%(levelname)s @ %(asctime)s: %(message)s; Lineno %(lineno)d, func %(funcName)s, file %(filename)s.', datefmt='%d/%m/%Y %H:%M:%S')

from hailey_data.INFO import PREFIX, VERSION

bot = commands.Bot(command_prefix=PREFIX)
"""
for extension in ("moderation", "roles", "joinleave"):
    extension = f"hailey_data.{extension}"
    bot.load_extension(extension)
    logging.info(f"LOADED EXTENTION {extension}")
"""
@bot.event
async def on_ready(): #TODO: Refactor
    print("Ready for action Rider sir!")
    final = ""
    for word in ["Paw", "Patrol", "Paw", "Patrol", "We'll", "be", "there", "on", "the", "double"]:
        for character in word:
            uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            lowercase = "abcdefghijklmnopqrstuvwxyz"
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
        final += " "
    final += "!"
    print(final)
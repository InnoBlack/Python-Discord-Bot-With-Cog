ilist = []


import os
os.system("title Discord Bot")

try:
    import discord
    from discord.ext import commands
except ImportError:
    os.system("pip install discord")
    os.system("pip install discord.py")
    import discord
    from discord.ext import commands

try:
    import tracemalloc
except ImportError:
    os.system("pip install tracemalloc")
    import tracemalloc

try:
    from colorama import Fore, init
except ImportError:
    os.system("pip install colorama")
    from colorama import Fore, init
try:
    import logging
except:
    os.system("pip install logging")
    import logging
from math import fabs
import time
import sys
from tracemalloc import stop

import load.on_bot_startup_ready


logging.basicConfig(level=logging.WARNING)
logging.getLogger("discord").setLevel(logging.WARNING)
logging.getLogger("discord.http").setLevel(logging.WARNING)
logging.getLogger("discord.gateway").setLevel(logging.WARNING)
logging.getLogger("discord.client").setLevel(logging.WARNING)
logging.getLogger("Requirement already satisfied:").setLevel(logging.WARNING)

init(autoreset=True)

def load_config():
    if os.path.exists("config\\token.txt"):
        with open("config\\token.txt", "r") as f:
            bottoken = f.read()
    else:
        bottoken = input("Your bot's token: ")
        with open("config\\token.txt", "w") as f:
            f.write(f"{bottoken}")
    ilist.append(bottoken)
    if os.path.exists("config\\prefix.txt"):
        with open("config\\prefix.txt", "r") as f:
            botprefix = f.read()
    else:
        botprefix = input("Your bot's prefix: ")
        with open("config\\prefix.txt", "w") as f:
            f.write(f"{botprefix}")
    ilist.append(botprefix)
    

load_config()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
tracemalloc.start()

async def load_commands():
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            await bot.load_extension(f'commands.{filename[:-3]}')
            time.sleep(0.200)
            print(f"{Fore.LIGHTBLACK_EX}[{time.strftime('%H:%M:%S')}]{Fore.RED} Loaded command: {Fore.LIGHTRED_EX}{filename[:-3]}")

async def load_events():
    for filename in os.listdir('./events'):
        if filename.endswith('.py'):
            await bot.load_extension(f'events.{filename[:-3]}')
            time.sleep(0.200)
            print(f"{Fore.LIGHTBLACK_EX}[{time.strftime('%H:%M:%S')}]{Fore.BLUE} Loaded event: {Fore.LIGHTCYAN_EX}{filename[:-3]}")

    
    print(f"{Fore.LIGHTBLACK_EX}[{time.strftime('%H:%M:%S')}]{Fore.LIGHTYELLOW_EX} All actions have been loaded")
    time.sleep(0.200)
    print(f"{Fore.LIGHTBLACK_EX}[{time.strftime('%H:%M:%S')}]{Fore.CYAN} All settings have been loaded")

@bot.event
async def on_ready():
    await load.on_bot_startup_ready.main_start(bot)
    print(f"{Fore.LIGHTBLACK_EX}[{time.strftime('%H:%M:%S')}]{Fore.LIGHTMAGENTA_EX} Logged in as {bot.user.name}")

async def setup():
    await load_commands()
    await load_events()

@bot.event
async def on_connect():
    await bot.wait_until_ready()
    await setup()

os.system("cls")
print(Fore.MAGENTA + "=" * 40)

while True:
    try:
        bot.run(f'{ilist[0]}', reconnect=True)
    except KeyboardInterrupt:
        print(Fore.RED + f"[{time.strftime('%H:%M:%S')}] Bot process terminated by user.")
        break
    except discord.LoginFailure:
        print(Fore.RED + f"[{time.strftime('%H:%M:%S')}] Invalid token. Please provide a valid bot token.")
        bottoken = input("Your bot's token: ")
        with open("config\\token.txt", "w") as f:
            f.write(f"{bottoken}")
    except Exception as e:
        os.system("cls")
        os.system("TASKKILL /F /PID %s" % os.getpid())

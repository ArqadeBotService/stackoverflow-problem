import discord
from discord.ext import commands
import json
from colorama import Back, Fore, Style
import time
import platform



def load_config():
    with open("config.json", "r", encoding="utf-8") as file:
        return json.load(file)

config  = load_config()



class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=config[prefix], intents=discord.Intents().all())

    async def on_ready(self):
        prfx = (Back.BLACK + Fore.GREEN + time.strftime("%H:%M:%S UTC", time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
        print(prfx + " Logged in as " + Fore.YELLOW + self.user.name)
        print(prfx + " Bot ID " + Fore.YELLOW + str(self.user.id))
        print(prfx + " Discord Version " + Fore.YELLOW + discord.__version__)
        print(prfx + " Python Version " + Fore.YELLOW + str(platform.python_version()))
        synced = await self.tree.sync()
        print(prfx + " Slash CMDs Synced " + Fore.YELLOW + str(len(synced)) + " Commands")
        
client = Client()

client.run(config["token"])

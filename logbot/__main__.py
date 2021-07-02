import os
import sys
import discord
import time

from dotenv import load_dotenv

from logbot.bot import LogBot
from logbot.helpers.log import info, fatal
from logbot.schedulers import LogChecker


load_dotenv()

PREFIX = os.getenv("PREFIX")
TOKEN = os.getenv("DISCORD_TOKEN")
FILE_TO_WATCH = os.getenv("FILE_TO_WATCH")
CHANNEL_ID = os.getenv("CHANNEL_ID")
if FILE_TO_WATCH:
    info("Watching file: " + FILE_TO_WATCH)
else:
    fatal("Please provide a FILE_TO_WATCH in your .env file")
    sys.exit()
if PREFIX:
    info("Start bot with prefix '" + PREFIX + "'")
else:
    fatal("Please provide a PREFIX in your .env file")
    sys.exit()
if CHANNEL_ID:
    info("Monitoring logs of text channel with ID " + CHANNEL_ID)
else:
    fatal("Please provide a CHANNEL_ID in your .env file")
    sys.exit()

bot = LogBot(PREFIX)

bot.load_extension("logbot.schedulers.LogChecker")


bot.remove_command("help")

bot.run(TOKEN)

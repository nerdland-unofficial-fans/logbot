import os
import sys
import discord
import time

from dotenv import load_dotenv

from logbot.bot import LogBot
from logbot.helpers.log import info, fatal
from logbot.schedulers import LogChecker
# from nerdlandbot.translations.Translations import get_text as _


load_dotenv()

PREFIX = os.getenv("PREFIX")
TOKEN = os.getenv("DISCORD_TOKEN")
FILE_TO_WATCH = os.getenv("FILE_TO_WATCH")
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

bot = LogBot(PREFIX)

bot.load_extension('logbot.schedulers.LogChecker')


# LogChecker.path_to_watch = os.path.join('.', 'logbot', 'test.txt')
# LogChecker.log_file = open(LogChecker.path_to_watch)
# LogChecker.old_log_contents = LogChecker.log_file.readlines()

# while True:   
#     new_log_contents = old_log.readlines()
#     added = [line for line in new_log_contents if not line in old_log_contents]
#     if added: 
#         print("Added: ", ", ".join (added))
#         # post message in text channel
#     old_log_contents = new_log_contents
#     time.sleep(1)

# LogChecker.check_logs.start(bot)
bot.remove_command("help")

bot.run(TOKEN)

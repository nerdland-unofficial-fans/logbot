import os
import sys
import discord
import requests
import time

from datetime import datetime, timedelta
from discord.ext import tasks, commands

from ..helpers.log import info, fatal


class LogChecker(commands.Cog, name = "Logchecker"):
    def __init__(self, bot):
        self.bot = bot
        print(os.getcwd())
        self.path = os.getenv("FILE_TO_WATCH")

        log_file = open(self.path)
        for offset, l in enumerate(log_file):
            pass
        self.offset = offset +1
        self.check_logs.start()
        log_file.close()
        
    # TODO make interval configurable
    @tasks.loop(seconds = 5.0)
    async def check_logs(self):
        info("Checking logs")
        log_file = open(self.path)

        new_log_contents = ''
        for new_offset, line in enumerate(log_file):
            if new_offset >= self.offset:
                new_log_contents += line

        self.offset = new_offset + 1
        log_file.close()
        
        if new_log_contents: 
            print("Added: ", new_log_contents)
            channel = self.bot.get_channel(808801637047992391)
            if channel:
                await channel.send('```autohotkey\n{}```'.format(new_log_contents))


    @check_logs.before_loop
    async def before_check_logs(self):
        print('waiting...')
        await self.bot.wait_until_ready()

def setup(bot: commands.Bot):
    bot.add_cog(LogChecker(bot))




from discord.ext.commands import Bot


class LogBot(Bot):
    def __init__(self, prefix: str):
        self.prefix = prefix
        super().__init__(command_prefix=self.prefix, case_insensitive=True)

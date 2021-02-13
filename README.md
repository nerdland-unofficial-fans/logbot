# logbot
This is a Python-based discord bot developed by the nerdland fan community to read the logs of the nerdlandbot.

# Roadmap
This bot was setup mostly as an experiment, and there is no clearly defined goal so far.
If you have any suggestions feel free to log an issue in this repository, any new ideas or challenges are much appreciated.

# Getting started
To get this project up and running, make sure you have the following installed:
- Python 3
- PIP
- [Poetry](https://python-poetry.org/docs/#installation)

Once you have these installed (you can check by running 'python --version', 'pip -V' and 'poetry -V' in a commandline) run the following command to install the required packages:
```
poetry install
```

You will also need to acquire a `DISCORD_TOKEN` for this to work. It is possible to obtain one with a developer account on Discord.

For using the YouTube notifications functionality you'll need to set the `YOUTUBE TOKEN` in your `.env` file. Follow the instructions [here](https://developers.google.com/youtube/registering_an_application) to create an API key.

You need to add a `FILE_TO_WATCH` to the .env file. This is the relative path of the log file of the nerdlandbot, as seen from the root folder of the logbot


You can now run the bot by running the following command:
```
python -m logbot
```

# Running this bot with docker

```
docker run -itd --restart="unless-stopped" --name nerdlandbot \
 -e PREFIX=<Your prefix here> \
 -e DISCORD_TOKEN=<Your discord token here> \
 -v <Your bind mount path for guild configs>:/GuildConfigs \
 nerdlandfansunofficial/nerdlandbot:latest
```

# Links
* [Nerdland website](https://nerdland.be)
* [Nerdland merch](https://www.mistert.be/nerdland)

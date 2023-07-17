#!/usr/bin/env bash

WEBSERVER=http://192.168.0.22:8888

# discord-stop

cd /home/pi/DiscordBot

rm main.py
rm functions.py
rm views.py
rm bot_commands.py
rm bot_slashcommands.py
rm index.html

wget $WEBSERVER/main.py
wget $WEBSERVER/functions.py
wget $WEBSERVER/views.py
wget $WEBSERVER/bot_commands.py
wget $WEBSERVER/bot_slashcommands.py
wget $WEBSERVER/index.html

wget $WEBSERVER/discord_update.sh
rm discord_update.sh
mv discord_update.sh.1 discord_update.sh
chmod +x discord_update.sh

# rm /home/pi/DiscordBot/sounds/random_sounds/*
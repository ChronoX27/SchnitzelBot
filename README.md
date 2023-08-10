# SchnitzelBot
## Requirements
 - Python 3.8 or above
 - Install the required python modules by running `pip install -r requirements.txt` (hope this works)
 - [Install ffmpeg](https://www.ffmpeg.org/):
    On Windows copy ffmpeg.exe in the *same folder* as main.py
    On Linux just install ffmepg and change `ffmpeg = ffmpeg.exe` to `ffmpeg = ffmpeg` in [.env](.env)
 - Edit [.env](.env) and replace `YOUR.BOT.TOKEN` with your token (you can get a token [here](https://discord.com/developers/applications))

## Start
 - You can start the bot by running `python main.py` while in the main folder of this project.
 - You might want to run the bot in the background. On Linux you can achieve this by using `nohub` like this: `nohub python3 ProjectFolder/main.py > LogFolder/nohub.log`
 - Change `prefix` for commands and your bots `status` in [.env](.env) as you like

## Usage
 - You can use slash commands definded in [bot_slashcommands.py](bot_slashcommands.py) with `/command_name`
 - You can use prefix commands too. They are definded in [bot_commands.py](bot_commands.py). Watch out to use the prefix definded in `.env`
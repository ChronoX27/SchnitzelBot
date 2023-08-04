# SchnitzelBot
## Requirements
 - [Install pycord](https://docs.pycord.dev/en/stable/installing.html) (NOT discord.py!)
 - [Install ffmpeg](https://www.ffmpeg.org/):
    On Windows copy ffmpeg.exe in the *same folder* as main.py
    On Linux just install ffmepg and change `"ffmpeg.exe"` to `"ffmpeg"` in [.env](.env)
 - Edit `.env` and replace `YOUR.BOT.TOKEN` with your token (you can get a token (here)[https://discord.com/developers/applications])
 - Install gTTS with `pip install gTTS` to use text-to-speach

## Start
 - You can start the bot by typing `python main.py` while in the main folder of this project.
 - You might want to run the bot in the background. On Linux you can achieve this by using `nohub` like this: `nohub python3 ProjectFolder/main.py > LogFolder/nohub.log ` 
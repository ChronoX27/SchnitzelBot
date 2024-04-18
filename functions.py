import requests
import json
import datetime


# --- READY ---
def ready(bot):
    print(f"====================== {bot.user} is ready ======================")

    date = str(datetime.datetime.now())[:-7]
    with open("log.txt", "a") as logfile:
        logfile.write(f"\n[{date}] reboot successfull")


# --- GET QUOTE ---
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    author = json_data[0]["a"]
    quote = json_data[0]["q"]
    return (quote, author)


# --- COMMAND LOG ---
def command_log(message, command, special_message=None):
    author = message.author
    channel = message.channel.name
    server = message.channel.guild.name

    date = str(datetime.datetime.now())[:-7]
    log_msg = f"[{date}] {author} used {command} on {server} in {channel}"

    if special_message:
        log_msg = f"{log_msg} {special_message}"

    print(log_msg)
    with open("log.txt", "a") as logfile:
        logfile.write("\n" + log_msg)


# --- ERORR LOG ---
def error_log(message, command, error_message):
    author = message.author
    date = str(datetime.datetime.now())[:-7]
    log_msg = f"[{date}] ERROR while {author} was using {command}:\
          {error_message}"

    # print(log_msg)
    with open("bot.log", "a") as myfile:
        myfile.write("\n" + log_msg)

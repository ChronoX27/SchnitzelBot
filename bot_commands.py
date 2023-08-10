import discord
import os
import dotenv
import math
import datetime
import gtts
import string
import random as rnd

from discord.ext import commands
from functions import command_log, error_log, get_quote
from views import *


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self._last_member = None

    # --- HI ---
    @commands.command(aliases=["hi"])
    async def hallo(self, ctx):
        """Begrüßt dich"""
        hallo = [
            "Hi",
            "Moin Moin",
            "Hallo du Lappen",
            "Servusle",
            "Guten Tag",
            "hello",
            "Grüß Gott",
            "Einen wunderschönen guten Tag, meine Damen und Herren",
        ]
        await ctx.send(rnd.choice(hallo))
        command_log(ctx, "hi")

    # --- TEST ---
    @commands.command()
    async def test(self, ctx):
        """Ein kleiner Test für den Bot"""
        await ctx.send("Funktioniert")
        command_log(ctx, "test")

    # --- ABOUT ---
    @commands.command()
    async def about(self, ctx):
        """kleine Info über den Bot"""
        embed = discord.Embed(
            title="SchnitzelBot",
            description="Always there if you need a Schnitzel \N{CUT OF MEAT}",
            color=discord.Colour.blurple()
        )
        
        embed.add_field(
            name="About this bot",
            value="A small Discord Bot with text and voice commands to experiment and have fun with friends.", 
            inline=False
        )

        embed.add_field(name="Author", value="Developed by ChronoX. [DM me](https://discordapp.com/users/716593329101602889)", inline=True)
        embed.add_field(name="GitHub", value="[View or clone the code](https://github.com/ChronoX27/SchnitzelBot)", inline=True)

        embed.set_thumbnail(url="https://github.com/ChronoX27/SchnitzelBot/blob/main/images/schnitzel.jpg?raw=true")
        await ctx.send("", embed=embed)
        command_log(ctx, "about")

    # --- HELP ---
    @commands.command()  # aliases=["help"])
    async def hilfe(self, ctx):
        """Du erhältst Hilfe"""
        commands = {
            ".hi": "Begrüßt dich",
            ".schnitzel": "Du bekommst ein Schnizel",
            ".help": "Du bekommst diese Nachricht",
            ".invite": "Du erhältst den Einladungslink zu diesem Bot",
            ".random": "Du erhältst eine zufällige Nachricht aus der serverübergreifenden Datenbank",
            ".add": "Füge eine neue Nachricht zur serverübergreifenden Datenbank hinzu",
            ".zitat/.quote": "Du erhältst ein sehr inspirierendes Zitat",
            ".wildschwein": "Gibt dir einen guten Ratschlag für dein Leben",
            ".bauer": "Ein herausragendes Zitat eines schlauen Menschens",
            ".crypto": "Bietet dir die Möglichkeit dieses Projekt zu unterstützen",
            ".mnf a b c": "Löst die quadratische Gleichung mit a*x² + b*x + c = 0",
            ".join": "Der Schnitzelbot kommt in deinen Voicechat",
            ".kran": "Lässt den Meister sprechen",
        }
        answer = ""
        for x in commands:
            answer = answer + x + "  -   " + commands[x] + "\n"

        await ctx.send(answer)
        command_log(ctx, "hilfe", "")

    # --- INVITE ---
    @commands.command()
    async def invite(self, ctx):
        """Der Einladungslink für diesen Bot"""
        await ctx.send("https://bit.ly/InviteSB")
        command_log(ctx, "invite")

    # --- QUOTE ---
    @commands.command(aliases=["zitat"])
    async def quote(self, ctx):
        """Du erhältst ein sehr inspirierendes Zitat"""
        quote, author = get_quote()
        
        quote_embed = discord.Embed(
            title="\N{Sparkles} Quote Time \N{sparkles}",
            description=f"„*{quote}*“\n ~ {author}",
            color=discord.Colour.from_rgb(107, 189, 214)
        )        
        quote_embed.set_thumbnail(url="https://github.com/ChronoX27/SchnitzelBot/blob/main/images/quote.jpg?raw=true")
        await ctx.respond("", embed=quote_embed)
        command_log(ctx, "quote", f"and got a quote by {author}")

    # --- SCHNITZEL ---
    @commands.command(aliases=["steak"])
    async def schnitzel(self, ctx):
        """Was geht über ein Schnitzel?"""
        steak = "\N{CUT OF MEAT}"
        message = f"{3 * (steak + ' ' )} SCHNITZEL HYPE {3 *('' + steak)} \nEs geht nichts über ein saftig-knaftiges Schnitzel! \n{3 * (steak + ' ' )} SCHNITZEL HYPE {3 *('' + steak)}"
        await ctx.send(message)
        command_log(ctx, "schnitzel")

    # --- BAUER ---
    @commands.command()
    async def bauer(self, ctx):
        """Ein herausragendes Zitat eines schlauen Menschens"""
        await ctx.send('"Da muss jeder mal schmunzeln"')
        command_log(ctx, "bauer")

    # --- WILDSCHWEIN ---
    @commands.command()
    async def wildschwein(self, ctx):
        """Gibt dir einen guten Ratschlag für dein Leben :boar:"""
        await ctx.send(
            "Pass auf Wildschweine auf, sie können zu unliebsamen Begegnungen führen"
        )
        command_log(ctx, "wildschwein")

    # --- CRYPTO ---
    @commands.command()
    async def crypto(self, ctx):
        """Bietet dir die Möglichkeit dieses Projekt zu unterstützen"""
        crypto = {
            "Bitcoin": "bc1qmkm5rm2f4dylcf3c5kr630940gtntf9pf9dcwt",
            "Bitcoin Cash": "ltc1qjtdl7ylksmax6zutwvrqhyl7mje56ygck5x6ra",
            "Ethereum": "0x885eE1D7a3bFc1bE0f1c49dD2D0f4f8A43Bb164D",
            "Litecoin": "ltc1qjtdl7ylksmax6zutwvrqhyl7mje56ygck5x6ra",
            "Polkadot": "18kvJccz36xkth458fXspkEFxzRFrPEtYftwtqm4UtjimvL",
            "Ripple": "rhmD5VWgBT73rCVuEYs8FuPv6UN1x6MPiu",
            "Solana": "8KeYwoY8BBumc1qysGSJsyVxc7wLPbn6G8NufzGh67DH",
            "Tezos": "tz1heKjcrTucWJiUMevttkqTTLeRBMkurvCy",
            "Tron": "TUoMo5jJZe9PQYgaM5Ks3nGgVE5XCGhocH",
            "Waves": "3P7AXSsV2CiXjsUjvbAs4W2eb6xqzqh2hZg",
        }
        answer = ""
        for x in crypto:
            answer += f"{x}  >>  {crypto[x]}\n"

        await ctx.send(answer)
        command_log(ctx, "crypto")

    # --- KRAN ---
    @commands.command()
    async def kran(self, ctx):
        """Lässt den Meister sprechen"""
        kranplatz = [
            "Siehste dat? Kranplatz... da soll ich jetzt 60 Tonnen drauf abstellen.",
            "Die Leute kommen einfach ihrer Arbeit nicht nach, das is dat Problem",
            "Die Leute kommen einfach ihrer Arbeit nicht nach, weil die, weiß ich nicht zu dumm sind, oder was...",
            "Kranplätze MÜSSEN verdichtet sein!",
            "Jetzt komm ich hier hoch, jetzt guck dir die Scheiße an. ",
            "Ham die Leute einfach keine Lust hier, oder wat?",
            "Du musst ma fragen, ob die... weiß ich nicht soll'n wir nach Hause fahr'n, oder wat?",
            "Is doch lächerlich, oder?",
            "Wissen doch, was so'n Kran wiegt, oder?",
            "Junge, jetzt krieg ich jetzt langsam hier... werd ich aber n bisschen wild hier, langsam.",
            "JETZT REICHT'S MIR LANGSAM! HAM DIE KEIN BANDMASS WAT ACHT METER LANG IS!?",
            "Junge, Junge, Junge, Junge, Junge, Junge, Junge, Junge, Junge, Junge!",
            "Oach Mensch, hör auf!",
            "Paar Nichtskönner, originale Nichtskönner",
            "Das is hier ne Baustelle für Vollidioten. Genau solche Vollidioten wie diese Norweger sind. VOLLIDIOTEN. Darum sind die auch nicht in der EU, weil die am Leben vorbeilaufen, diese Spinnerbande.",
            "Gar nichts zusammenpacken, Ende!",
            "Können noch nicht mal BANDMASS halten!",
        ]
        answer = kranplatz[rnd.randint(0, len(kranplatz) - 1)]

        await ctx.send(answer)
        command_log(ctx, "kran")

    # --- MNF ---
    @commands.command()
    async def mnf(self, ctx, arg1, arg2, arg3):
        """.mnf a b c: Löst die quadratische Gleichung mit a*x² + b*x + c = 0"""
        a = float(arg1)
        b = float(arg2)
        c = float(arg3)
        await ctx.send(f"a = {a};  b = {b};  c = {c}")

        if (b * b - 4 * a * c) < 0:
            await ctx.send("Die Gleichung hat keine Lösungen.")
        elif (b * b - 4 * a * c) == 0:
            x = (-b - math.sqrt(b * b - 4 * a * c)) / 2 * a
            await ctx.send(f"Diese Gleichung hat nur eine Lösung: \n  x = {x}")
        else:
            x1 = (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a
            x2 = (-b - math.sqrt(b * b - 4 * a * c)) / 2 * a
            await ctx.send(
                f"Die Lösungen dieser Gleichung sind: \n  x1 = {x1}\n  x2 = {x2}"
            )

        command_log(ctx, "mnf")

    # --- RANDOM ---
    @commands.command()
    async def random(self, ctx):
        """Erhalte eine zufällig Nachricht aus der Datenbank"""
        lines = open("random.txt", "r", encoding="utf-8").read().splitlines()
        line_number = rnd.randint(0, len(lines))
        random_line = lines[line_number]

        await ctx.send(f"Nachricht Nummer {line_number}: \n{random_line}")
        command_log(ctx, "random", f"and got message number {line_number}")

    # --- ADD ---
    @commands.command()
    async def add(self, ctx, message):
        """Füge der Datenbank eine Nachricht hinzu"""
        print(message)

        date = datetime.datetime.now()
        date = f'{date.strftime("%d")}.{date.strftime("%b")}.{date.strftime("%Y")}'

        random_message = f"{message} ~ {str(ctx.author)[:-5]} ({date})"
        with open("random.txt", "a") as file:
            file.write(f"\n{random_message}")
        await ctx.send(
            f"Du hast der Datenbank folgende Nachricht hinzugefügt: \n{message}"
        )
        command_log(ctx, "add", f"and added '{message}'")

    # ---JOIN ---
    @commands.command(aliases=["vc", "connect"])
    async def join(self, ctx):
        """Der Schnitzelbot tritt deinem Voicechannel bei"""
        voice_channel = ctx.author.voice.channel
        if voice_channel == None:
            await ctx.send("Du befindest dich nicht in einem Voice-Channel")
            command_log(ctx, "join", "but no voice channel was found")
            error_log(
                ctx,
                "join",
                f"Could not find {ctx.author}s voice channel on {ctx.guild}",
            )
            return

        await voice_channel.connect()
        await ctx.send("Hallöchen :wave:", view=Leave())
        command_log(ctx, "join")

    # --- HARDSTYLE ---
    @commands.command()
    async def hardstyle(self, ctx):
        """kurze, aber feine Party"""

        dotenv.load_dotenv()
        ffmpeg = os.environ.get("ffmpeg")

        is_voice = ctx.author.voice
        if is_voice == None:
            await ctx.send(
                "Du befindest dich nicht in einem Voice-Channel auf diesem Server"
            )
            command_log(ctx, "hardstyle", "but no voice channel was found")
            error_log(
                ctx,
                "hardstyle",
                f"Could not find {ctx.author}s voice channel on {ctx.guild}",
            )
            return

        voice_channel = ctx.author.voice.channel
        try:
            await voice_channel.connect()
        except:
            print(" >> Already connected to voice")
        voice = ctx.guild.voice_client

        try:
            voice.play(
                discord.FFmpegPCMAudio(
                    executable=ffmpeg, source="sounds/lebendiger_fisch.mp3"
                )
            )
        except:
            await ctx.send("Whoops, da gab es wohl einen Fehler D:")
            error_log(ctx, "hardstyle", "Couldn't play sound")
            command_log(ctx, "hardstyle", "but an error occured while playing a sound")
            return

        await ctx.send("Are you readyyyyy? Let's go!", view=VoiceView())
        command_log(ctx, "hardstyle")

    # --- READ ---
    @commands.command(aliases=["tts"])
    async def read(self, ctx, message, language="de"):
        """Tipp: gib deine Nachricht in Anführungszeichen ein :)"""

        dotenv.load_dotenv()
        ffmpeg = os.environ.get("ffmpeg")

        tts = gtts.gTTS(message, lang=language.lower())
        name = "".join(rnd.choice(string.ascii_letters) for i in range(12))
        soundfile = f"sounds/random_sounds/{name}.mp3"
        tts.save(soundfile)

        is_voice = ctx.author.voice
        if is_voice == None:
            await ctx.send("Du befindest dich nicht in einem Voice-Channel")
            command_log(ctx, "read", "but no voice channel was found")
            error_log(
                ctx,
                "read",
                f"Could not join {ctx.author}s voice channel on {ctx.guild}",
            )
            return

        voice_channel = ctx.author.voice.channel
        try:
            await voice_channel.connect()
        except:
            print(" >> Cant connect to voice")
        voice = ctx.guild.voice_client

        voice.play(discord.FFmpegPCMAudio(executable=ffmpeg, source=soundfile))
        voice.source.volume = 1.0
        await ctx.send(f"Ich lese nun: {message}", view=VoiceView())
        command_log(ctx, "read", f"and read '{message}' in {language}")

    # --- JOSUA ---
    @commands.command()
    async def josua(self, ctx):
        """Ein Junge mit einer gottesgleichen Stimme trällert dir ein Liedchen"""

        dotenv.load_dotenv()
        ffmpeg = os.environ.get("ffmpeg")

        is_voice = ctx.author.voice
        if is_voice == None:
            await ctx.send(
                "Du befindest dich nicht in einem Voice-Channel auf diesem Server"
            )
            command_log(ctx, "josua", "but no voice channel was found")
            error_log(
                ctx,
                "josua",
                f"Could not find {ctx.author}s voice channel on {ctx.guild}",
            )
            return

        voice_channel = ctx.author.voice.channel
        try:
            await voice_channel.connect()
        except:
            print(" >> Already connected to voice")

        voice = ctx.guild.voice_client

        rickroll = rnd.randint(0, 99)

        if rickroll == 0:
            soundfile = "sounds/ricky.mp3"
            message = "F"
            special_message = "and got rickrolled"
        else:
            soundfile = "sounds/josua.mp3"
            message = "JOOOOSUA, aufstehen, es ist null Uhr nachts!"
            special_message = None

        try:
            voice.play(discord.FFmpegPCMAudio(executable=ffmpeg, source=soundfile))
        except:
            await ctx.send("Whoops, da gab es wohl einen Fehler D:")
            error_log(ctx, "josua", "Couldn't play sound")
            command_log(ctx, "josua", "but an error occured while playing a sound")
            return

        await ctx.send(message, view=VoiceView())
        command_log(ctx, "josua", special_message)

    # --- LEAVE ---
    @commands.command(aliases=["disconnect"])
    async def leave(self, ctx):
        """Der SchnitzelBot verlässt deinen Voicechannel wieder"""
        voice_client = ctx.guild.voice_client
        await voice_client.disconnect()
        command_log(ctx, "leave")

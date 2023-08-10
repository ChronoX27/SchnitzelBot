import discord
import os
import dotenv
import datetime
import gtts
import string
import random as rnd

from discord.ext import commands
from functions import command_log, error_log, get_quote
from views import *


class Slashcommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # --- TEST ---
    @commands.slash_command()
    async def test(self, ctx):
        """Ein kleiner Test für den Bot"""
        await ctx.respond("Funktioniert")
        command_log(ctx, "/test")

    # --- BUTTON ---
    @commands.slash_command()
    async def button(self, ctx):
        await ctx.respond("Touch that button!", view=MyView())
        command_log(ctx, "/button")

    # --- ABOUT ---
    @commands.slash_command()
    async def about(self, ctx):
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

        embed.set_thumbnail(url="https://github.com/ChronoX27/SchnitzelBot/blob/2eb14da7458f04cd73b0ad470d1d176e5268bc7a/images/schnitzel.jpg?raw=true")
        await ctx.respond("", embed=embed)
        command_log(ctx, "/about")

    # --- HALLO ---
    @commands.slash_command(alias=["hi"])
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
        await ctx.respond(rnd.choice(hallo))
        command_log(ctx, "/hallo")

    # --- HI ---
    @commands.slash_command()
    async def hi(self, ctx):
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
        await ctx.respond(rnd.choice(hallo))
        command_log(ctx, "/hi")

    # --- HELP ---
    # TODO: HELP

    # --- INIVTE ---
    @commands.slash_command()
    async def invite(self, ctx):
        """Der Einladungslink für diesen Bot"""
        await ctx.respond("https://bit.ly/InviteSB")
        command_log(ctx, "/invite")

    # --- ZITAT ---
    @commands.slash_command(aliases=["zitat"])
    async def quote(self, ctx):
        """Du erhältst ein sehr inspirierendes Zitat"""
        quote, author = get_quote()
        await ctx.respond(quote)
        command_log(ctx, "/quote", f"and got a quote by {author}")

    # --- SCHNITZEL ---
    @commands.slash_command(aliases=["steak"])
    async def schnitzel(self, ctx):
        """Was geht über ein Schnitzel?"""
        steak = "\N{CUT OF MEAT}"
        message = f"{8 * (steak + ' ')} \nEs geht nichts über ein saftig-knaftiges Schnitzel! \n{8 * (steak + ' ')}"
        await ctx.respond(message)
        command_log(ctx, "/schnitzel")

    # --- BAUER ---
    @commands.slash_command()
    async def bauer(self, ctx):
        """Ein herausragendes Zitat eines schlauen Menschens"""
        await ctx.respond('"Da muss jeder mal schmunzeln"')
        command_log(ctx, "/bauer")

    # --- WILDSCHWEIN ---
    @commands.slash_command()
    async def wildschwein(self, ctx):
        """Gibt dir einen guten Ratschlag für dein Leben \N{BOAR}"""
        await ctx.respond(
            "Pass auf Wildschweine auf, sie können zu unliebsamen Begegnungen führen"
        )
        command_log(ctx, "/wildschwein")

    # --- CRYPTO ---
    @commands.slash_command()
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

        await ctx.respond(answer)
        command_log(ctx, "/crypto")

    # --- KRAN ---
    @commands.slash_command()
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

        await ctx.respond(answer)
        command_log(ctx, "/kran")

    # --- MNF ---
    # TODO: MNF

    # --- RANDOM ---
    @commands.slash_command()
    async def random(self, ctx):
        """Erhalte eine zufällig Nachricht aus der Datenbank"""
        lines = open("random.txt", "r", encoding="utf-8").read().splitlines()
        line_number = rnd.randint(0, len(lines))
        random_line = lines[line_number]

        await ctx.respond(f"Nachricht Nummer {line_number}: \n{random_line}")
        command_log(ctx, "/random", f"and got message number {line_number}")

    # --- ADD ---
    @commands.slash_command()
    async def add(self, ctx, message):
        """Füge der Datenbank eine Nachricht hinzu"""
        date = datetime.datetime.now()
        date = f'{date.strftime("%d")}.{date.strftime("%b")}.{date.strftime("%Y")}'

        random_message = f"{message} ~ {str(ctx.author)[:-5]} ({date})"
        with open("random.txt", "a") as file:
            file.write(f"\n{random_message}")
        await ctx.respond(
            f"Du hast der Datenbank folgende Nachricht hinzugefügt: \n{message}"
        )
        command_log(ctx, "/add", f"and added '{message}'")

    # --- JOIN ---
    @commands.slash_command()
    async def join(self, ctx):
        """Der Schnitzelbot tritt deinem Voicechannel bei"""
        voice_channel = ctx.author.voice.channel
        if voice_channel == None:
            await ctx.send("Du befindest dich nicht in einem Voice-Channel")
            command_log(ctx, "/join", "but no voice channel was found")
        else:
            await voice_channel.connect()
            await ctx.respond("Hallöchen :wave:", view=Leave())
            command_log(ctx, "/join")

    # --- JOSUA ---
    @commands.slash_command()
    async def josua(self, ctx):
        """Ein Junge mit einer gottesgleichen Stimme trällert dir ein Liedchen"""

        dotenv.load_dotenv()
        ffmpeg = os.environ.get("ffmpeg")

        is_voice = ctx.author.voice
        if is_voice == None:
            await ctx.respond(
                "Du befindest dich nicht in einem Voice-Channel auf diesem Server"
            )
            command_log(ctx, "/josua", "but no voice channel was found")
            error_log(
                ctx,
                "/josua",
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
            await ctx.respond("Whoops, da gab es wohl einen Fehler D:")
            error_log(ctx, "/josua", "Couldn't play sound")
            command_log(ctx, "/josua", "but an error occured while playing a sound")
            return

        await ctx.respond(message, view=VoiceView())
        command_log(ctx, "/josua", special_message)

    # --- HARDSTYLE ---
    @commands.slash_command()
    async def hardstyle(self, ctx):
        """kurze, aber feine Party"""

        dotenv.load_dotenv()
        ffmpeg = os.environ.get("ffmpeg")

        is_voice = ctx.author.voice
        if is_voice == None:
            await ctx.respond(
                "Du befindest dich nicht in einem Voice-Channel auf diesem Server"
            )
            command_log(ctx, "/hardstyle", "but no voice channel was found")
            error_log(
                ctx,
                "/hardstyle",
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
            await ctx.respond("Whoops, da gab es wohl einen Fehler D:")
            error_log(ctx, "/hardstyle", "Couldn't play sound")
            command_log(ctx, "/hardstyle", "but an error occured while playing a sound")
            return

        await ctx.respond("Are you readyyyyy? Let's go!", view=VoiceView())
        command_log(ctx, "/hardstyle")

    # --- READ ---
    @commands.slash_command(aliases=["tts"])
    async def read(self, ctx, message, language="de"):
        """Gib die Sprache als optionales Argument ein"""

        dotenv.load_dotenv()
        ffmpeg = os.environ.get("ffmpeg")

        tts = gtts.gTTS(message, lang=language.lower())
        name = "".join(rnd.choice(string.ascii_letters) for i in range(12))
        soundfile = f"sounds/random_sounds/{name}.mp3"
        tts.save(soundfile)

        is_voice = ctx.author.voice
        if is_voice == None:
            await ctx.respond("Du befindest dich nicht in einem Voice-Channel")
            command_log(ctx, "/read", "but no voice channel was found")
            error_log(
                ctx,
                "/read",
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
        await ctx.respond(f"Ich lese nun: {message}", view=VoiceView())
        command_log(ctx, "/read", f"and read '{message}' in {language}")

    # --- LEAVE ---
    @commands.slash_command(aliases=["disconnect"])
    async def leave(self, ctx):
        """Der SchnitzelBot verlässt deinen Voicechannel wieder"""
        await ctx.respond("Auf Wiedersehen")
        voice_client = ctx.guild.voice_client
        await voice_client.disconnect()
        command_log(ctx, "/leave")

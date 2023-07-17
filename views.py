import discord

# ----------- VIEWS -----------
class MyView(discord.ui.View):
    @discord.ui.button(label="click me!", style=discord.ButtonStyle.primary)
    async def button_callback(self, Button, interaction):
        print(" >> CLICK!")
        await interaction.response.send_message("You just clicked the Button")

# --- VOICE VIEW ---
class VoiceView(discord.ui.View):
    @discord.ui.button(label="Leave", row=0, style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction):
        voice_client = interaction.guild.voice_client
        await voice_client.disconnect()
        await interaction.response.send_message("Bye Bye")
        print(" >> left the voice chat")

    @discord.ui.button(label="Stop", row=1, style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction):
        interaction.guild.voice_client.pause()
        print(" >> Stopped the sound")
        await interaction.response.send_message("Stopped :pause_button:")

# --- JUST LEAVE ---
class Leave(discord.ui.View):
    @discord.ui.button(label="Leave", style=discord.ButtonStyle.red)
    async def button_callback(self, button, interaction):
        voice_client = interaction.guild.voice_client
        await voice_client.disconnect()
        await interaction.response.send_message("Bye Bye :wave:")
        print(" >> left the voice chat")


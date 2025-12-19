import discord
from aiohttp.web_routedef import options
from discord import *
import ffmpeg
import discord.app_commands

print('OpenTTSBOTv2.py - \nCreated by Yuki Ito')
print("Bot is initializing...")

with open('config.json', 'r') as f:
    import json
    config = json.load(f)
    TOKEN = config['token']
    TESTGUILDID = config['test-guild-id']
TESTGUILD = None

intents = discord.Intents.default()
intents.messages = True

bot = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(bot)

@bot.event
async def on_ready():
    await tree.sync()
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    TESTGUILD = discord.Object(id=TESTGUILDID)

@tree.command(name="ping", description="Replies with Pong!")
async def ping(interaction: discord.Interaction):
    print('ping command received')
    await interaction.response.send_message("Pong!")

@tree.command(name='info', description='このBOTの情報を表示します。', guild=TESTGUILD)
async def info(interaction: discord.Interaction):
    print('info command received')
    embed = discord.Embed(title="OpenTTSBOTv2", description="This is a Discord bot for TTS using OpenTTS.", color=0x00ff00)
    embed.add_field(name="Version", value="2.0", inline=False)
    embed.add_field(name="Creator", value="Yuki Ito", inline=False)
    await interaction.response.send_message(embed=embed)




bot.run(TOKEN)
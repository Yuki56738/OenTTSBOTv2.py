import discord
from aiohttp.web_routedef import options
from discord import *
import ffmpeg
import discord.app_commands
from discord.ext import *

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
    global TESTGUILD
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    TESTGUILD = discord.Object(id=TESTGUILDID)
    await tree.sync(guild=TESTGUILD)

@tree.command(name="ping", description="Replies with Pong!")
async def ping(interaction: discord.Interaction):
    print('ping command received')
    await interaction.response.send_message("Pong!")

@tree.command(name='info', description='このBOTの情報を表示します。', guild=discord.Object(id=TESTGUILDID))
async def info(interaction: discord.Interaction):
    print('info command received')
    # embed = discord.Embed(title="OpenTTSBOTv2", description="This is a Discord bot for TTS using OpenTTS.", color=0x00ff00)
    # embed.add_field(name="Version", value="2.0", inline=False)
    # embed.add_field(name="Creator", value="Yuki Ito", inline=False)
    # await interaction.response.send_message(embed=embed)
    # embed = discord.Embed(title='Created by Yuki.', description = 'バージョン: 0.1', color = 0x6fbfd3)
    # embed.set_author(name='OpenTTSBOTv2', url='https://risaton.net')
    # await interaction.response.send_message(embed=embed)
    embed = discord.Embed(title="OpenTTSBOTv2 v0.1",
                          description="Created by Yuki.",
                          colour=0x474fbd)

    embed.add_field(name="コマンド",
                    value="/join で読み上げを開始します。\n/leave で終了します。",
                    inline=False)
    embed.add_field(name="このボットについて",
                    value="yuki1999によって作られた、オープンソースの読み上げBOTです！\ndiscordの仕様の移り変わりにて、以前のものは使えなくなってしまいましたが、1から作り直しました。",
                    inline=False)

    await interaction.response.send_message(embed=embed)


bot.run(TOKEN)
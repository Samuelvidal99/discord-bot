import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import ffmpeg
from utils import *
from time import sleep
import json
from random import randrange

load_dotenv()



DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='$')

user_greeting = True
data = {}
with open('./data/data.json') as file:
    data = json.load(file)

@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        global servidor 
        servidor = guild
        guild_count = guild_count + 1
        print(f"- {guild.id} (name: {guild.name})")

    print("ZapZapBot is in " + str(guild_count) + " guilds.")


@bot.event
async def on_voice_state_update( member : discord.Member, before : discord.VoiceState, after : discord.VoiceState):
    if member.id == data['users_id']['vitor']:
        if before.channel == None:
            await member.voice.channel.connect()
            audio_converted = discord.FFmpegOpusAudio("/app/audios/teste.mp4", executable="/app/ffmpeg")

            voice_client = get_voice_client_member(member.voice.channel, bot.voice_clients)

            sleep(2)
            voice_client.play(audio_converted)
            sleep(16)
            await voice_client.disconnect()
            
    else:
        global user_greeting
        if (member.id != bot.user.id) and user_greeting:
            if before.channel == None:
                guild = get_guild(member.voice.channel, bot.guilds)
                sleep(2)
                index = randrange(0,3)
                message = data["greeting_messages"][index]
                await guild.text_channels[0].send(
                    f"{member.name} {message}", 
                    tts=True, 
                    delete_after=10.0
                )


@bot.command()
async def clear(ctx, amount = 11):
    await ctx.channel.purge(limit = amount)


@bot.command()
async def zapzap(ctx):
    voice_channel = get_voice_channel_author(ctx)

    await voice_channel.connect()
    audio_converted = discord.FFmpegOpusAudio(source="/app/audios/zapzap.mp4", executable="/app/ffmpeg")

    voice_client = get_voice_client_member(voice_channel, bot.voice_clients)
    voice_client.play(audio_converted)

    await ctx.channel.send(data["messages"]["zapzap_command"])

    index = randrange(0,len(data["gifs"]))
    await ctx.channel.send(data["gifs"][index])

    sleep(37)
    await voice_client.disconnect()


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.channel.send(
            data["errors"]["author_not_found_through_voice_channel"],
            delete_after=10.0
        )


@bot.command()
async def user_greeting(ctx, *, message):
    global user_greeting

    if message == "True":
        user_greeting = True
    elif message == "False":
        user_greeting = False


bot.run(DISCORD_TOKEN)
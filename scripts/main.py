import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import ffmpeg

load_dotenv()

def get_voice_client_member(channel, voice_clients):
    for voice_client in voice_clients:
        if voice_client.channel.id == channel.id:
            return voice_client


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix=';;')

@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        global servidor
        servidor = guild

        guild_count = guild_count + 1
        print(f"- {guild.id} (name: {guild.name})")

    print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

# @bot.event
# async def on_voice_state_update( member : discord.Member, before : discord.VoiceState, after : discord.VoiceState):
#     if member.display_name == "SamuelVidal99":
#         if before.channel == None:
#             await member.voice.channel.connect()
#             audio_converted = discord.FFmpegOpusAudio("test.wmv.mp3", executable="./scripts/ffmpeg.exe")

#             global voice_client
#             voice_client = get_voice_client_member(member.voice.channel, bot.voice_clients)
            
#             # voice_client.play(audio_converted)
#             print(voice_client.channel)
#             print(await audio_converted.probe(audio_converted))
#             print(audio_converted.is_opus())
#             print(audio_converted.read())

@bot.command()
async def clear(ctx, amount = 11):
    await ctx.channel.purge(limit = amount)


@bot.command()
async def test(ctx):
    await ctx.channel.send("Teste Louco")

@bot.command()
async def teste(ctx):
    await servidor.voice_channels[0].connect()

    print(servidor.voice_channels)

    print("teste")

    audio_converted = discord.FFmpegOpusAudio(source="teste.wmv.mp3", executable="./ffmpeg.exe")

    print(audio_converted.read())
    print(audio_converted.is_opus())
    bot.voice_clients[0].play(audio_converted)

    print(bot.voice_clients[0].is_playing())

    print("teste")


bot.run(DISCORD_TOKEN)
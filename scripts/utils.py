import discord



def get_voice_client_member(channel, voice_clients):
    for voice_client in voice_clients:
        if voice_client.channel.id == channel.id:
            return voice_client

def get_guild(channel, guilds):
    for guild in guilds:
        if guild.id == channel.guild.id:
            return guild

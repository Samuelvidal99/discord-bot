import discord



def get_voice_client_member(channel, voice_clients):
    for voice_client in voice_clients:
        if voice_client.channel.id == channel.id:
            return voice_client

def get_guild(channel, guilds):
    for guild in guilds:
        if guild.id == channel.guild.id:
            return guild

def get_voice_channel_author(ctx):
    for voice_channel in ctx.guild.voice_channels:
        print(voice_channel.name)
        for member in voice_channel.members:
            print("teste")
            print(member)
            # if member.id == ctx.author.id:
            #     return voice_channel
import discord


# Função que retorna o voice_client do bot a partir de um channel.
def get_voice_client_member(channel, voice_clients):
    for voice_client in voice_clients:
        if voice_client.channel.id == channel.id:
            return voice_client

# Função que retorna a guild que um channel pertence.
def get_guild(channel, guilds):
    for guild in guilds:
        if guild.id == channel.guild.id:
            return guild

# Função que retorna o voice_channel que o author do commando está conectado.
def get_voice_channel_author(ctx):
    for voice_channel in ctx.guild.voice_channels:
        for member in voice_channel.members:
            if member.id == ctx.author.id:
                return voice_channel
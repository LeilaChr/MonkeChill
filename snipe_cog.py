import discord
from discord.ext import commands


class snipe_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        bot.sniped_messages = {}
        @bot.event
        async def on_message_delete(message):
            bot.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)
            try:
                contents, author, channel_name, time = bot.sniped_messages[message.guild.id]
                
            except:
                return
        
            embed = discord.Embed(description=contents, color=discord.Color.purple(), timestamp=time)
            embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
            embed.set_footer(text=f"Deleted in : #{channel_name}")
            channel = bot.get_channel(966397399704682556)
            await channel.send(embed=embed)
        
        @bot.command()
        async def snipe(ctx):
            try:
                contents, author, channel_name, time = bot.sniped_messages[ctx.guild.id]
                
            except:
                await ctx.channel.send("Couldn't find a message to snipe!")
                return
        
            embed = discord.Embed(description=contents, color=discord.Color.purple(), timestamp=time)
            embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
            embed.set_footer(text=f"Deleted in : #{channel_name}")
        
            await ctx.channel.send(embed=embed)
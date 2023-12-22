import discord
from creds import token
import os
intents = discord.Intents.default()
intents.members = True  

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} is online!")

@client.event
async def on_member_join(member):
    channel = member.guild.system_channel  
    if channel is not None:
        embed = discord.Embed(
            title=f"Welcome {member.display_name}!",
            description="Welcome to the Frost Hacks server, We're excited to have you here!",
            color=discord.Color.green()
        )
        gif_path = "./gif.gif"  
        if os.path.exists(gif_path):
            embed.set_thumbnail(url="attachment://" + os.path.basename(gif_path))
            await channel.send(embed=embed, file=discord.File(gif_path, filename=os.path.basename(gif_path)))
        else:
            await channel.send("GIF not found.")


client.run(token)

import discord
from creds import token
intents = discord.Intents.default()
intents.on_member_join = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_member_join(member):
    channel = member.guild.system_channel  # Fetching the system channel
    if channel is not None:
        embed = discord.Embed(
            title=f"Welcome {member.display_name}!",
            description="Welcome to our Discord server! We're excited to have you here.",
            color=discord.Color.green()
        )
        embed.set_thumbnail(url=member.avatar_url)
        await channel.send(embed=embed)

# Replace 'YOUR_TOKEN_HERE' with your bot's token
client.run(token)

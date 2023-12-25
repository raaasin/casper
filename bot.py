from pydoc import replace
import discord
from creds import token,key
import os
import google.generativeai as genai


genai.configure(api_key=key)
intents = discord.Intents.default()
intents.members = True  

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} is online!")

@client.event
async def on_member_join(member):
    channel_id = 1158623747205509142  
    channel = client.get_channel(channel_id)

    if channel is not None:
        embed = discord.Embed(
            title=f"Welcome {member.display_name}!",
            description="Welcome to the Frost Hacks server, We're excited to have you here!",
            color=discord.Color.purple()
        )
        gif_path = "./assets/gif.gif"  

        if os.path.exists(gif_path):
            embed.set_thumbnail(url="attachment://" + os.path.basename(gif_path))
            await channel.send(embed=embed, file=discord.File(gif_path, filename=os.path.basename(gif_path)))
        else:
            await channel.send("GIF not found.")


"""
def get_message(message):
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    response = chat.send_message(message, stream=True)
    response.resolve()
    return response

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg=replace(message.content,"<@1187776872680009849>","")
    answer = get_message(msg)
    for chunk in answer:
        await message.channel.send(chunk.text)
"""
    
client.run(token)

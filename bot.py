import discord
from creds import token
import os
import random

intents = discord.Intents.default()
intents.members = True  

client = discord.Client(intents=intents)

welcome_messages = [
    "Welcome to Frosthacks, our hackathon wonderland in the digital snowscape! Get ready to code in a winter paradise! ❄️",
    "Hey there, hackers! Step into our frosty hackathon—where snow and code combine for an icy adventure! ❄️",
    "Welcome aboard Frosthacks! Join us in hacking through the snow to create something extraordinary! ⚙️❄️",
    "Greetings, coding snowflakes! Enter Frosthacks, where tech and snow meet for an epic hackathon experience! ❄️💻",
    "Welcome to Frosthacks, where innovative ideas snowball into groundbreaking projects! Let's hack away! ❄️🚀",
    "Ahoy, hackers! Welcome to Frosthacks—brace yourselves for a snowstorm of coding brilliance! ❄️💻",
    "Welcome to our digital snowbank, Frosthacks edition! Get ready for a hackathon under the frosty skies! ❄️☁️",
    "Hello and welcome to Frosthacks! Grab your code editor and let's craft some snow-powered solutions! ❄️💡",
    "Welcome, coding enthusiasts! At Frosthacks, we're snow-excited to see your hackathon magic! ❄️✨",
    "Step into Frosthacks, our snowy hackathon wonderland! Time to code and create frosty innovations! ❄️💻✨",
    "Welcome, coding wizards! Prepare for a snow-filled journey of hackathon challenges and breakthroughs! ❄️🧙‍♂️✨",
    "Greetings, newcomer hackers! The snowflakes here are code fragments waiting to build wonders! ❄️💻✨",
    "Welcome to Frosthacks, where each line of code melts away barriers! Make yourself at home! ❄️💻🏠",
    "Hello and a warm snowflake welcome to Frosthacks! Get ready for a hackathon like no other! ❄️❤️",
    "Welcome to our digital snow sanctuary—Frosthacks edition! Let's code, innovate, and conquer! ❄️💻🏰",
    "Hey there, tech enthusiasts! Welcome to our server where hackathon spirits meet frosty camaraderie! ❄️👋",
    "Greetings, new hacker friend! Your presence here just made our hackathon server even more epic. Welcome! ❄️🚀",
    "Welcome to Frosthacks—our snow-covered hub for tech innovation and coding marvels! ❄️💻🏔️",
    "Hey, you made it to Frosthacks! Let's huddle together and create hackathon wonders in the snow! ❄️🤝",
    "Welcome, welcome, one and all to Frosthacks! Your arrival just made our snowy hackathon even cooler! ❄️🎉",
    "Welcome to Frosthacks, where the snowflakes of innovation fall upon the code! Let's create wonders! ❄️✨",
    "Hey there, coding snow wizards! Enter Frosthacks and let the hackathon adventures begin in our wintry realm! ❄️🧙‍♂️✨",
    "Welcome aboard Frosthacks! Brace yourself for a snow-filled hackathon journey where ideas flurry! ❄️🚀",
    "Greetings, tech snowboarders! At Frosthacks, we carve code into snow-covered innovations! ❄️🏂💻",
    "Welcome to Frosthacks, the icy playground where code and snowflakes blend into brilliant hacks! ❄️💻🌨️",
    "Ahoy, tech explorers! Get ready for a coding blizzard at Frosthacks—an epic hackathon awaits! ❄️🌬️💻",
    "Welcome to our digital snowbank, Frosthacks edition! Gear up for a hackathon under the frosty sky! ❄️💻☁️",
    "Hello and a snowy welcome to Frosthacks! Let's embark on a hackathon journey through the snow! ❄️🚀",
    "Welcome, coding snow sculptors! At Frosthacks, craft your code into frosty hackathon masterpieces! ❄️💻🎨",
    "Step into Frosthacks, where snowflakes code and create extraordinary hackathon innovations! ❄️💻✨",
    "Welcome, tech architects! Prepare for a frosty hackathon journey filled with snowy challenges! ❄️🏗️💻",
    "Greetings, coding mountaineers! Climb the peaks of innovation at Frosthacks—it's hackathon time! ❄️⛰️💻",
    "Welcome to Frosthacks, where each line of code is a snowflake in our flurry of innovation! ❄️💻✨",
    "Hello and a warm hackathon welcome to Frosthacks! Embrace the snow as we craft code wonders! ❄️💻❤️",
    "Welcome to our digital snow sanctuary—Frosthacks edition! Let's code, innovate, and conquer! ❄️💻🏰",
    "Hey there, tech snowballers! In our server, hackathon spirits meet in a flurry of innovation! ❄️💻🎉",
    "Greetings, new coding comrades! Your presence just made our hackathon server even more epic. Welcome to Frosthacks! ❄️💻🤝",
    "Welcome to Frosthacks—our snowy workshop for tech innovation and coding marvels! ❄️💻🛠️",
    "Hey, you've reached Frosthacks! Let's huddle together and create hackathon wonders in the snow! ❄️🤝🎉",
    "Welcome, welcome, one and all to Frosthacks! Your arrival just made our snowy hackathon even cooler! ❄️🎉👋"
]


@client.event
async def on_ready():
    print(f"{client.user} is now online!")

@client.event
async def on_member_join(member):
    channel_id = 1158623747205509142  
    channel = client.get_channel(channel_id)

    if channel is not None:
        embed = discord.Embed(
            title=f"Welcome {member.display_name}!",
            description=member.mention + " "+ str(random.choice(welcome_messages)),
            color=discord.Color.purple()
        )

        embed.set_thumbnail(url=member.display_avatar.url)
        await channel.send(embed=embed)

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

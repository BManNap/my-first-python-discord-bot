# bot.py
#creater discord ******
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = "Token-of-bot"

client = discord.Client()



@client.event
async def on_ready():
    print(
        f'{client.user} is connected to the following guild:\n'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    funky_message = [
    os.system("dig +short myip.opendns.com @resolver1.opendns.com > ip.txt")
    ]
    if message.content == "cool":
        response = random.choice(funky_message)
        os.system("dig +short myip.opendns.com @resolver1.opendns.com > ip.txt")
        var = os.popen('cat ip.txt').read()
        await message.channel.send(os.popen('cat ip.txt').read())
        print(message.author)
        print(var)
        pass




client.run(TOKEN)

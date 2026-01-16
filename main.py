import discord
import os

# Set up intents for the bot
intents = discord.Intents.default()
intents.message_content = True  # Allows the bot to read message content

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged on as {client.user}!')

@client.event
async def on_message(message):
    # Don't respond to ourselves
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# Using DISCORD_TOKEN as a standard secret name
token = os.getenv('DISCORD_TOKEN') or os.getenv('TOKEN')
if token:
    client.run(token)
else:
    print("Please set your DISCORD_TOKEN secret in the Secrets tab.")

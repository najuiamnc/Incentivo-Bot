import discord
import os 

# Define the intents your bot needs
# Intents.default() includes basic things like guild join/leave
# message_content is needed to read what's in a message
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event  
async def on_ready(): 
   print(f'We have logged in as {client.user}') 

@client.event
async def on_message(message):
  # Don't respond to ourselves
  if message.author == client.user:  
      return

  if message.content.startswith('$hello'):  
      await message.channel.send('Hello!')

# Use 'DISCORD_TOKEN' as a more standard name, but fallback to 'TOKEN'
token = os.getenv('DISCORD_TOKEN') or os.getenv('TOKEN')
if token:
    client.run(token)
else:
    print("Error: No bot token found. Please add 'DISCORD_TOKEN' to your Secrets.")

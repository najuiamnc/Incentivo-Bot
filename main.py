import discord
import os 
import requests 
import json 

# Define the intents your bot needs
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    # Corrected the syntax error and the typo 'jason_data'
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote
    
@client.event  
async def on_ready(): 
   print(f'We have logged in as {client.user}') 

@client.event
async def on_message(message):
    # Don't respond to ourselves
    if message.author == client.user:  
        return

    if message.content.startswith('$inspire'): 
        quote = get_quote()
        await message.channel.send(quote)
    
    if message.content.startswith('$hello'):  
        await message.channel.send('Hello!')

# Use 'DISCORD_TOKEN' as a more standard name, but fallback to 'TOKEN'
token = os.getenv('DISCORD_TOKEN') or os.getenv('TOKEN')
if token:
    client.run(token)
else:
    print("Error: No bot token found. Please add 'DISCORD_TOKEN' to your Secrets.")

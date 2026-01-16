import discord
import os 
import requests 
import json 
import random

# Define the intents your bot needs
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Fixed the variable assignment from '-' to '='
sad_words = ['estou triste', 'triste', 'deprimido', 'mal', 'chorei', 'bravo', 'desanimado', 'desmotivado', 'desapontado', 'sozinho', 'desesperado', 'desamparado', 'desinteressado', 'desinteressada', 'desinteressados']

starter_encouragements = [
    'Eu te amo!', 
    'Você é incrível!', 
    'Você é o melhor!', 
    'Eu acredito em você!', 
    'Você é forte!', 
    'Você é especial!', 
    'Tenho orgulho de você!'
]
             
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    # Fixed syntax error: changed '=' to '+' and 'jason_data' to 'json_data'
    quote = json_data[0]['q'] + ' - ' + json_data[0]['a']
    return quote
    
@client.event  
async def on_ready(): 
   print(f'We have logged in as {client.user}') 

@client.event
async def on_message(message): 
    if message.author == client.user:  
        return

    msg = message.content.lower()

    if msg.startswith('$inspire'): 
        quote = get_quote()
        await message.channel.send(quote)

    if msg.startswith('$hello'):  
        await message.channel.send('Hello!')

    # Fixed typos: 'chanel' to 'channel' and 'choise' to 'choice'
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

# Use 'DISCORD_TOKEN' as a more standard name, but fallback to 'TOKEN'
token = os.getenv('DISCORD_TOKEN') or os.getenv('TOKEN')
if token:
    client.run(token)
else:
    print("Error: No bot token found. Please add 'DISCORD_TOKEN' to your Secrets.")

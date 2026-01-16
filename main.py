import discord
import os
import requests
import json
import random
from replit import db

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Added missing commas in sad_words list
sad_words = [
    'estou triste', 'triste', 'deprimido', 'mal', 'chorei',
    'bravo', 'desanimado', 'desmotivado', 'desapontado', 'sozinho',
    'desesperado', 'desamparado', 'desinteressado', 'desinteressada',
    'desinteressados', 'não quero mais viver', 'depressao', 'ansiedade', 
    'irritado', 'irritada'
]

# Added missing commas in starter_encouragements list
starter_encouragements = [
    'Eu te adoro!', 'Você é incrível!', 'Você é o melhor!',
    'Eu acredito em você!', 'Você é forte!', 'Você é especial!',
    'Tenho orgulho de você!', 'Vamos jogar um jogo?',
    'Sinto sua falta todos os dias!'
]

def get_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        # FIXED: Changed '=' to '+' and fixed 'jason_data' typo
        quote = json_data[0]['q'] + ' - ' + json_data[0]['a']
        return quote
    except Exception as e:
        print(f"Error fetching quote: {e}")
        return "Tudo vai ficar bem! Continue em frente."

def update_encouragements(encouraging_message):
    if 'encouragements' in db.keys():
        encouragements = db['encouragements']
        encouragements.append(encouraging_message)
        db['encouragements'] = encouragements
    else:
        db['encouragements'] = [encouraging_message]

def delete_encouragement(index):
    if 'encouragements' in db.keys():
        encouragements = db['encouragements']
        if len(encouragements) > index:
            del encouragements[index]
            db['encouragements'] = encouragements

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
        await message.channel.send('Olá! Como posso ajudar hoje?')

    options = starter_encouragements
    if 'encouragements' in db.keys():
        # Ensure we convert the db object to a list for concatenation
        options = options + list(db['encouragements'])

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))

    if msg.startswith('$new'):
        encouraging_message = msg.split('$new ', 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send('New encouraging message added.')

    if msg.startswith('$del'):
        encouragements = []
        if 'encouragements' in db.keys():
            try:
                index = int(msg.split('$del ', 1)[1])
                delete_encouragement(index)
                encouragements = list(db['encouragements'])
            except (ValueError, IndexError):
                pass
        await message.channel.send(encouragements)

token = os.getenv('DISCORD_TOKEN') or os.getenv('TOKEN')
if token:
    client.run(token)
else:
    print("Error: No bot token found. Please add 'DISCORD_TOKEN' to your Secrets.")

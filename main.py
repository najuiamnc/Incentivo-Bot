import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

sad_words = [
    'estou triste', 'triste', 'deprimido', 'mal', 'chorei',
    'bravo', 'desanimado', 'desmotivado', 'desapontado', 'sozinho',
    'desesperado', 'desamparado', 'desinteressado', 'desinteressada',
    'desinteressados', 'não quero mais viver', 'depressao', 'ansiedade',
    'irritado', 'irritada'
]

starter_encouragements = [
    'Eu te adoro!', 'Você é incrível!', 'Você é o melhor!',
    'Eu acredito em você!', 'Você é forte!', 'Você é especial!',
    'Tenho orgulho de você!', 'Vamos jogar um jogo?',
    'Sinto sua falta todos os dias!'
]

if 'responding' not in db.keys():
    db['responding'] = True

def get_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
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

    if db['responding']:
        options = starter_encouragements
        if 'encouragements' in db.keys():
            options = options + list(db['encouragements'])

        if any(word in msg for word in sad_words):
            await message.channel.send(random.choice(options))
    
    if msg.startswith('$new'):
        try:
            encouraging_message = message.content.split('$new ', 1)[1]
            update_encouragements(encouraging_message)
            await message.channel.send('New encouraging message added.')
        except IndexError:
            await message.channel.send('Please include a message to add.')
    
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

    if msg.startswith('$list'):
        encouragements = []
        if 'encouragements' in db.keys():
            encouragements = list(db['encouragements'])
        await message.channel.send(encouragements)

    if msg.startswith('$responding'):
        try:
            value = msg.split('$responding ', 1)[1]
            if value.lower() == 'true':
                db['responding'] = True
                await message.channel.send('Responding is on.')
            else:
                db['responding'] = False
                await message.channel.send('Responding is off.')
        except IndexError:
            status = 'on' if db['responding'] else 'off'
            await message.channel.send(f"Responding is currently {status}.")

keep_alive()
token = os.getenv('DISCORD_TOKEN') or os.getenv('TOKEN')
if token:
    client.run(token)
else:
    print("Error: No bot token found. Please add 'DISCORD_TOKEN' to your Secrets.")

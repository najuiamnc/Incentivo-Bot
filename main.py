import discord
import os

# To use this bot, you'll need to add your bot token as a secret named 'DISCORD_TOKEN'
# You can do this in the 'Secrets' tab (lock icon) in the sidebar.

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # Don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

token = os.getenv('DISCORD_TOKEN')
if token:
    client.run(token)
else:
    print("Please set your DISCORD_TOKEN secret.")

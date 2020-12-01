import discord

token = "NzgzMjA2NjgwNzIwMzEwMjkz.X8XYDw.n47Xp8_-UFBjjHMnTk-Dp8i7Pso"

client = discord.Client() 


@client.event 
async def on_ready(): 
    print(f'We have logged in as {client.user}') 


@client.event
async def on_message(message): 

    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    if "!hello" in message.content.lower():
        await message.channel.send('Hi!')
    if "!you sus" in message.content.lower():
        await message.channel.send('no u')
    if "!developer" in message.content.lower():
        await message.channel.send('ItzCool is the developer of this bot, honestly he sus')
    if "!among us" in message.content.lower():
        await message.channel.send('Best Game EVER CREATED ON EARTH')
    if "!f in the chat" in message.content.lower():
        await message.channel.send('F')
    if "!who are you" in message.content.lower():
        await message.channel.send('I AM GENERAL SUS! NOW START RUNNIN LAPS OR YOU WILL NEVER OUTRUN THE IMPOSTOR!')
    if str(message.author) == "ItzCool#1786" and "!take control" in message.content.lower():
        while True:
            await message.channel.send(input('send message : '))
client.run(token)  

import discord
import difflib
token = "NzgzMjA2NjgwNzIwMzEwMjkz.X8XYDw.1q7saPjInjtu7QcmdM4zPaT_Cc8"
client = discord.Client()
f = open("text_commands.txt",'r')
text = f.read()
tex = text.split("\n")
commands = []
responses = []
for i in tex:
    kl = i.split()
    commands.append(kl[0])
    responses.append(" ".join(kl[1:]))
f.close()
@client.event 
async def on_ready(): 
    print(f'We have logged in as {client.user}') 


@client.event
async def on_message(message): 

    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    # Searches the command in the text file and responds as given.
    if message.content.lower()[0] == "!" and message.content.lower() in commands and str(message.author) != "General Sus#7352":
        response = responses[commands.index(message.content.lower())]
        await message.channel.send(response)
    
    # gets prediction possibility.
    if message.content.lower()[0] == "!" and not message.content.lower() in commands and message.content.lower() != "!help":
        await message.channel.send("Command not working. Did you mean : "+difflib.get_close_matches(message.content.lower(),commands)[0] )
    # Make a command using a command ( for the dev )
    if message.content.lower().split()[0] == "@makecommand" and str(message.author) == "ItzCool#1786":
        f = open("text_commands.txt",'a')
        f.write("\n"+ message.content.lower().split()[1] + " " + " ".join(message.content.lower().split()[2:]))
        f.close()
        commands.append(message.content.lower().split()[1])
        responses.append(" ".join(message.content.lower().split()[2:]))
    # Delete a command ( for the dev )
    if message.content.lower().split()[0] == "@deletecommand" and str(message.author) == "ItzCool#1786":
        ind = commands.index(message.content.lower().split()[1])
        del commands[ind]
        del responses[ind]
        text = "" 
        for i in range(len(commands)):
            text += commands[i] + " "+ responses[i] + "\n"
        f = open("text_commands.txt","w")
        
        f.write(text[0:-1])

        f.close()
        await message.channel.send("Command deleted")
    # help on commands
    if message.content.lower().split()[0] == "!help":
        for i in commands:
            await message.channel.send(i)
    # Dev Control.
    if str(message.author) == "ItzCool#1786" and "!take control" in message.content.lower():
        
        while True:
            try:
                await message.channel.send(input('send message : '))
            except:
                break
    
client.run(token)  

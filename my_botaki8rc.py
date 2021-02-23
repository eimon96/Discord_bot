import discord
import random
from discord.ext import commands


TOKEN = "" #ADD bots token
#GUILD = "" #ADD servers name and uncomment below


client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} is alive!!')

    
#    for guild in client.guilds:
#        if guild.name == GUILD:
#            break

#    print(
#        f'{client.user} is connected to the following guild:\n'
#        f'{guild.name}(id: {guild.id})'
#    )



# ------------------------------------------------------------ #    
"""    
bot = commands.Bot(command_prefix='!')

@bot.command(name='96')
async def nine_six(ctx):
    
    respobot = ['I am just a bot, not a threat.']

    response = random.choice(respobot)
    await ctx.channel.send(response)
        
bot.run(TOKEN)
"""
# ------------------------------------------------------------ #



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    respo = ['ante gamhsou', 'malaka', 'me enoxleis', 'gamw to spitaki sou',
            'gamw th mana sou', 'na fas skata', 'eisai athlios programmatisths',
            'hlithie', 'mpetovlaka', 'skase', 'stamata na milas', 'kathisterimene',
            'voulwse to', 'minara', 'h python gamaei, esu oxi', 'autoktona']
    
    if message.content == "eisai uiothetimeno":
        response = "kai esu autistiko"
        await message.channel.send(response)
    elif message.content.startswith("den eimai"):
        response = "eisai"
        await message.channel.send(response)
    elif (message.content.find("kalos") != -1) and (message.content.find("programmatisths") != -1):
        response = "arxidia eisai"
        await message.channel.send(response)
    elif (message.content.find("eixa") != -1) and (message.content.find("duskolh") != -1) and (message.content.find("mera") != -1):
        response = "sta arxidia mou"
        await message.channel.send(response)
    elif message.content.startswith(""):
        response = random.choice(respo)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException
  
  
  
  
client.run(TOKEN)



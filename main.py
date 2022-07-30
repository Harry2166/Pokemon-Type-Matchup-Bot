import os
import discord
from keep_alive import keep_alive
import pokemon_typings as pt

client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
#https://discord.com/api/oauth2/authorize?client_id=986208224166428703&permissions=274878105600&scope=bot
  if message.content.startswith('!pokemon'):
    await message.channel.send("Greetings! You have summoned the Pokemon Typing Bot.\nKindly type '!monotype [type]' or '!dualtype [type1] [type2]' depending on what kind of typing you would like to know the strengths and weaknesses.\n")

  if message.content.startswith('!monotype'):
    monotype = message.content.split('!monotype ')[1].title()
    
    if monotype in pt.types:
      index_monotype = pt.types.index(monotype)
      await message.channel.send(f"Strengths: {', '.join(pt.strength[index_monotype])}\nWeaknesses: {', '.join(pt.weakness[index_monotype])}")
      
    else:
      await message.channel.send("Please input a valid pokemon typing.")

  if message.content.startswith('!dualtype'):
    dualtype = message.content.split('!dualtype ')[1]
    dualtype1 = dualtype.split(" ")[0].title()
    dualtype2 = dualtype.split(" ")[1].title()
    
    if dualtype1 == dualtype2:
      await message.channel.send("Please type two unique typings")
      
    elif dualtype1 and dualtype2 in pt.types:
      
      index_dualtype1 = pt.types.index(dualtype1)
      index_dualtype2 = pt.types.index(dualtype2)

      overall_weakness = []
      overall_strength = []
        
      resistance_immunities = [] 

      for typing in pt.strength[index_dualtype1]:
          overall_strength.append(typing)

      for typing in pt.strength[index_dualtype2]:
          overall_strength.append(typing)

      for typing in pt.weakness[index_dualtype1]:
          overall_weakness.append(typing) 

      for typing in pt.weakness[index_dualtype2]:
          overall_weakness.append(typing)
        
      for typing in overall_weakness:
          if typing in pt.immunities[index_dualtype1] or typing in pt.immunities[index_dualtype2]:
              resistance_immunities.append(typing)
          elif typing in pt.resistances[index_dualtype1] or typing in pt.resistances[index_dualtype2]:
              resistance_immunities.append(typing)
          
      await message.channel.send(f"Strengths: {', '.join(list((set(overall_strength))))}\nWeaknesses: {', '.join(list((set(overall_weakness)) - set(resistance_immunities)))}")
    else:
      await message.channel.send("Please input a valid pokemon type or type combination")

print("Hello!")
  
my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)

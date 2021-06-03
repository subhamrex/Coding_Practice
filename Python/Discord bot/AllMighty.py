import discord
import asyncio
import requests
import json
import random

client = discord.Client()

TOKEN = "ODIxMTA5MzAyMDA5NzkwNDc1.YE-7oQ.6bUR9LpAzN9C69PYMe6tNCkboJc"

sad_words = ['sad','depressed','unhappy','miserable','depressing']

hero_quotes = ['Don\'t be sad because I am here','Trick your situation','Peace']

def get_quote():
  res = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(res.text)
  quote = json_data[0]['q'] + " ~"+ json_data[0]['a']
  return quote

@client.event
async def on_ready():
  print(f"We are logged in as {client.user}")

@client.event
async def on_message(messaage):
  if messaage.author == client.user:
    return
  msg = messaage.content

  if msg.startswith("#hello"):
    await messaage.channel.send('All Mighty is here!')

  if msg.startswith("#command"):
    await messaage.channel.send('#hello --> Greeting \n#inspire --> get random inpire quote')

  if msg.startswith("#inspire"):
    quote = get_quote()
    await messaage.channel.send(quote)   
    
  if any(word in msg for word in sad_words ):
      await  messaage.channel.send(random.choice(hero_quotes))
 
       

client.run(TOKEN)


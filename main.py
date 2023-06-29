from pyrogram import Client
from os import getenv
import poe
import json

api_id = int(getenv("api_id"))
api_hash = getenv("api_hash")
client = poe.Client(getenv("bot_token"))

bot = Client(name="new-client-bot",api_id=api_id,api_hash=api_hash)

@bot.on_message()
async def test_bot(client, message):
  s = message.text
  if "سروش" in s or "soroush" in s:
    for chunk in await client.send_message("soroushbot", s):
      pass
    await message.reply(chunk["text"])

bot.run() 

from pyrogram import Client
from os import getenv

Hungry = True

api_id = getenv("api_id")
api_hash = getenv("api_hash")

def splitter(s, c):
    res = []
    for i in s:
        res.append(i.split(c))
    return res

def List(s):
    string = " ،,‌."
    res = s.split()
    for char in string:
        res = splitter(res, char)
    return res


bot = Client(name="new-client-bot",api_id=api_id,api_hash=api_hash)
good = List(input("Enter your list of must-have words:"))
bad = List(input("Enter your list of banned words:"))

def check(s):
  s = s.split()
  global good, bad
  for i in good:
    if(not i in s):
      return 0
  for i in bad:
    if(i in s):
      return 0
  return 1

@bot.on_message()
async def test_bot(client, message):
  global Hungry
  print(message.chat)
  s = message.text
  if Hungry and check(s):
    await message.reply('استفاده')
    await bot.send_message(message.from_user.id, 'سلام\nوقتتون بخیر\nاستفاده')
    Hungry = False
  if message.text == '!activate':
    Hungry = True
    await message.reply('Bot activated ✅')
  if message.text == '!deactivate':
    Hungry = True
    await message.reply('Bot dactivated ❌')
  if message.text == '!status':
    if Hungry:
      await message.reply('Bot is active ✅')
    else:
      await message.reply("Bot isn't active ❌")

bot.run() 

from pyrogram import Client
from os import getenv

Hungry = True
Testing = False

api_id = int(getenv("api_id"))
api_hash = getenv("api_hash")

def splitter(s, c):
    res = []
    for i in s:
        nw = i.split(c)
        for j in nw:
            res.append(j)
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
  global Hungry, Testing
  #print(message.chat)
  s = message.text
  if Hungry and check(s) and (Testing or message.chat.id == -1001147339220):
    await message.reply('استفاده')
    await bot.send_message(message.from_user.id, 'سلام\nوقتتون بخیر\nاستفاده')
    Hungry = False
  if message.text == '!Testing-mode':
    Testing = not Testing
    if Testing:
      await message.reply('Testing mode on ✅')
    else:
      await message.reply('Testing mode off ❌')
  if Testing:
    Hungry = True
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

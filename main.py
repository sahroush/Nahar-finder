from pyrogram import Client
status = True

api_id = 22675233
api_hash = "324ef3f73ba621dfac2cad87be556d21"

bot = Client(name="new-client-bot",api_id=api_id,api_hash=api_hash)
#nice = list(input("good words:").split())
#bad = list(input("bad words:").split())
nice = list("فنی بالا دارم".split())
bad = list("بالا معاوضه میخوام میخام تعویض عوض درخواستی".split())

def good(s):
  s = s.split()
  global nice, bad
  for i in nice:
    if(not i in s):
      return 0
  for i in bad:
    if(i in s):
      return 0
  return 1

@bot.on_message()
async def test_bot(client, message):
  global status
  #if message.text in ('hello'):
  s = message.text
  if status and good(s):
    #print(message)
    await message.reply('استفاده')
    await bot.send_message(message.from_user.id, 'سلام\nوقتتون بخیر\nاستفاده')
    status = False
  if message.text == '!active':
    status = True
    await message.reply('Bot activated ✅')
  if message.text == '!deactive':
    status = True
    await message.reply('Bot dactivated ❌')
  if message.text == '!status':
    if status:
      await message.reply('Bot is active ✅')
    else:
      await message.reply("Bot isn't active ❌")

bot.run() 

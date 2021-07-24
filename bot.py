from googletrans import Translator

translator = Translator()

text1 = "cyka blyat"
dt1 = translator.detect(text1)
print(dt1)
if dt1.lang == "ru":
    print("Yay!")
else:
    print("Not yay :(")
import discord

class MyClient(discord.Client):
    async def on_ready(self):
#        print('Logged in as')
#        print(self.user.name)
#        print(self.user.id)
#        print('------')
#    async def on_message(self, message):
#        #await message.channel.send("bruh bruh bruh")
#        if message.channel.id == CHANNEL_ID :
#            print("bruh")
#            if message.author.id == self.user.id:
#                return
#            else:
#                inp = message.content
#                name = message.author.display_name
#                print(inp)
#                bruh = translator.translate(inp)
#                sendbruh = bruh.text
#                channel = client.get_channel(844935359216746509)
#                final = name + ": " + sendbruh
#                await channel.send(final)

#client = MyClient()
#client.run('TOKEN')

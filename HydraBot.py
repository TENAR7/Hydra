from pyrogram import Client, filters



api_id = "25880728"
api_hash = 'a820a04ae1fda255ff9b83d5a7aa7ebf'
bot_token = '5643113953:AAEM6rCnlJzLNGalTHiEa1p8CwqfFw6F5sI'


app = Client("Youebot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


@app.on_message(filters.private)
async def hello(client, message):
   await message.reply("Don't send any messages!\n\nBot is under development")


app.run()
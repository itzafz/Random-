import random
from pyrogram import Client, filters

API_ID = 24597778
API_HASH = "0b34ead62566cc7b072c0cf6b86b716e"
BOT_TOKEN = "8291404941:AAGEEhSkqddqakx1Vpc3-_bnQopehvC3Yoc"

app = Client("guess-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

user_data = {}

@app.on_message(filters.command("start"))
def start(client, message):
    user_data[message.from_user.id] = random.randint(1, 500)
    message.reply("🎯 Guess a number between 1 and 500\nUse: /guess 123")

@app.on_message(filters.command("guess"))
def guess(client, message):
    try:
        guess_num = int(message.text.split()[1])
        target = user_data.get(message.from_user.id)

        if not target:
            target = random.randint(1, 500)
            user_data[message.from_user.id] = target

        if guess_num > target:
            message.reply("🔼 Too High!")
        elif guess_num < target:
            message.reply("🔽 Too Low!")
        else:
            message.reply("🎉 Correct Guess!")
            user_data[message.from_user.id] = random.randint(1, 500)

    except:
        message.reply("❌ Use format: /guess 123")

app.run()

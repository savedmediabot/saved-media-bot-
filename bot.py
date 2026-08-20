import telebot
from yt_dlp import YoutubeDL

BOT_TOKEN = "8307611188:AAG3A0DLG_ME5P2qup-CH2ZLB6qDCwjWheQ"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Menga video havolasini yuboring, men yuklab beraman!")

@bot.message_handler(func=lambda message: True)
def download_video(message):
    url = message.text
    if "http" in url:
        msg = bot.reply_to(message, "Video yuklanmoqda, kuting...")
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'video.mp4',
            'quiet': True
        }
        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            with open('video.mp4', 'rb') as video:
                bot.send_video(message.chat.id, video, caption="@savedmessagers_bot")
            bot.delete_message(message.chat.id, msg.message_id)
        except Exception as e:
            bot.edit_message_text("Videoni yuklab bo'lmadi. Havolani tekshirib ko'ring.", message.chat.id, msg.message_id)

bot.infinity_polling()

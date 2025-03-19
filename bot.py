from telegram import Update, WebAppInfo
from telegram.ext import Application, CommandHandler

TOKEN = "توکن ربات"

async def start(update: Update, context):
    keyboard = [[{"text": "🔥 باز کردن مینی اپ", "web_app": WebAppInfo(url="https://your-username.github.io/your-repo/")}]]
    await update.message.reply_text("برای باز کردن مینی اپ، روی دکمه زیر کلیک کن:", reply_markup={"keyboard": keyboard, "resize_keyboard": True})

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("ربات اجرا شد...")
app.run_polling()

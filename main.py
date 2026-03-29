import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import yt_dlp

BOT_TOKEN = os.getenv("8602137933:AAGrs2DtixA-9AUp66DiFi03_uiBhq0UYHQ")

async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    await update.message.reply_text("⏳ Downloading...")

    try:
        ydl_opts = {'format': 'best', 'outtmpl': 'video.%(ext)s'}

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        await update.message.reply_video(video=open(filename, 'rb'))
        os.remove(filename)

    except:
        await update.message.reply_text("❌ Failed")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, download_video))
app.run_polling()

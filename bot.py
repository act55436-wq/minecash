import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("8301691786:AAHcQ6BTLX91LmbSW-XEFCrlR2vuS8Lxtlg")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to MineCash!\n\n"
        "⛏️ Earn coins by watching ads & mining.\n"
        "💰 Open Dashboard 👇\n"
        "https://act55436-wq.github.io/minecash/"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()

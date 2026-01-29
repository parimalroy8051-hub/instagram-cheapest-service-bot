import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

BOT_TOKEN = os.getenv("8188938308:AAEaf7geyzXdnsBVDOmlAYQdSYOXCwuoruA")
FORCE_CHANNEL = os.getenv("@onlyearnfreee")  # like @channelusername


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    if FORCE_CHANNEL:
        try:
            member = await context.bot.get_chat_member(FORCE_CHANNEL, user.id)
            if member.status in ["left", "kicked"]:
                btn = [[InlineKeyboardButton("Join Channel", url=f"https://t.me/{FORCE_CHANNEL.replace('@','')}")]]
                await update.message.reply_text(
                    "❌ আগে আমাদের চ্যানেল Join করো",
                    reply_markup=InlineKeyboardMarkup(btn)
                )
                return
        except:
            pass

    await update.message.reply_text(
        "✅ Bot working!\n\nWelcome 😄"
    )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()


if __name__ == "__main__":
    main()

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8188938308:AAEaf7geyzXdnsBVDOmlAYQdSYOXCwuoruA"
FORCE_CHANNEL = "@onlyearnfreee"
OWNER_USERNAME = "@DigitalTricks_Support"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    try:
        member = await context.bot.get_chat_member(FORCE_CHANNEL, user.id)
        if member.status in ["left", "kicked"]:
            keyboard = [
                [InlineKeyboardButton("🔔 Join Channel", url="https://t.me/onlyearnfreee")]
            ]
            await update.message.reply_text(
                "❌ আগে আমাদের চ্যানেলে Join করুন\nতারপর আবার /start দিন",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
            return
    except:
        await update.message.reply_text(
            "⚠️ Bot কে channel এ Admin করতে হবে"
        )
        return

    await update.message.reply_text(
        f"👋 Welcome {user.first_name}!\n\n"
        "✅ Bot এখন ঠিকভাবে কাজ করছে\n\n"
        f"👨‍💻 Owner: {OWNER_USERNAME}"
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Start bot\n"
        "/help - Help\n\n"
        f"Support: {OWNER_USERNAME}"
    )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    print("🤖 Bot started")
    app.run_polling()


if __name__ == "__main__":
    main()

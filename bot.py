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
            buttons = [
                [InlineKeyboardButton("✅ Join Channel", url="https://t.me/onlyearnfreee")],
                [InlineKeyboardButton("👤 Owner", url="https://t.me/DigitalTricks_Support")]
            ]
            await update.message.reply_text(
                "❌ আগে Channel Join করো তারপর bot ব্যবহার করতে পারবে",
                reply_markup=InlineKeyboardMarkup(buttons)
            )
            return
    except:
        pass

    await update.message.reply_text(
        "✅ Bot Successfully Running!\n\n/use commands"
    )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 BOT STARTED")
    app.run_polling()


if __name__ == "__main__":
    main()

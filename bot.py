import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# ================= CONFIG =================
BOT_TOKEN = "8188938308:AAEaf7geyzXdnsBVDOmlAYQdSYOXCwuoruA"
FORCE_CHANNEL = "@onlyearnfreee"   # without https://t.me/
OWNER_USERNAME = "@DigitalTricks_Support"
# =========================================


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    # Force channel join check
    try:
        member = await context.bot.get_chat_member(FORCE_CHANNEL, user.id)
        if member.status in ["left", "kicked"]:
            btn = [
                [InlineKeyboardButton("🔔 Join Channel", url=f"https://t.me/{FORCE_CHANNEL.replace('@','')}")],
                [InlineKeyboardButton("✅ Joined", callback_data="joined")]
            ]
            await update.message.reply_text(
                "❌ আগে আমাদের চ্যানেলে Join করুন তারপর আবার /start দিন",
                reply_markup=InlineKeyboardMarkup(btn)
            )
            return
    except Exception:
        await update.message.reply_text(
            "⚠️ চ্যানেল চেক করতে সমস্যা হচ্ছে!\n"
            "Bot কে আগে চ্যানেলে Admin করুন।"
        )
        return

    # Main welcome message
    await update.message.reply_text(
        f"👋 স্বাগতম {user.first_name}!\n\n"
        "✅ আপনি সফলভাবে Bot ব্যবহার করতে পারছেন।\n\n"
        f"👨‍💻 Owner: {OWNER_USERNAME}"
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ Help Menu\n\n"
        "/start - Bot চালু করুন\n"
        "/help - সাহায্য\n\n"
        f"Support: {OWNER_USERNAME}"
    )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))

    print("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()

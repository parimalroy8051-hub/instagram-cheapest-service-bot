from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import os

# ================= CONFIG =================
BOT_TOKEN = os.environ.get("8188938308:AAEaf7geyzXdnsBVDOmlAYQdSYOXCwuoruA")
FORCE_CHANNEL = os.environ.get("@onlyearnfreee")  # @channelusername
OWNER_USERNAME = "@DigitalTricks_Support"  # চাইলে বদলাতে পারো
# =========================================


def start(update: Update, context: CallbackContext):
    user = update.effective_user

    try:
        member = context.bot.get_chat_member(FORCE_CHANNEL, user.id)
        if member.status in ["left", "kicked"]:
            raise Exception("Not joined")
    except:
        keyboard = [
            [InlineKeyboardButton("✅ Join Channel", url=f"https://t.me/{FORCE_CHANNEL.replace('@','')}")],
            [InlineKeyboardButton("🔁 Check Again", callback_data="check")]
        ]
        update.message.reply_text(
            "❌ আগে আমাদের channel join করতে হবে!",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    keyboard = [
        [InlineKeyboardButton("📦 Instagram Services", callback_data="services")],
        [InlineKeyboardButton("📞 Contact Owner", url=f"https://t.me/{OWNER_USERNAME.replace('@','')}")]
    ]

    update.message.reply_text(
        "👋 Welcome!\n\nনিচের option থেকে বেছে নাও 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == "check":
        start(query, context)

    elif query.data == "services":
        query.edit_message_text(
            "📦 *Instagram Cheapest Services*\n\n"
            "• Followers\n"
            "• Likes\n"
            "• Views\n\n"
            "Order করতে owner এর সাথে কথা বলো 👇",
            parse_mode="Markdown"
        )


def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

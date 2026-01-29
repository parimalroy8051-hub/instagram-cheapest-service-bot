from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)
import os

# ================== CONFIG ==================
BOT_TOKEN = "8188938308:AAEaf7geyzXdnsBVDOmlAYQdSYOXCwuoruA"
FORCE_CHANNEL = "@onlyearnfreee"
OWNER_USERNAME = "@DigitalTricks_Support"
# ============================================


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    # Force join check
    if FORCE_CHANNEL:
        try:
            member = await context.bot.get_chat_member(FORCE_CHANNEL, user.id)
            if member.status in ["left", "kicked"]:
                buttons = [
                    [InlineKeyboardButton("✅ Join Channel", url=f"https://t.me/{FORCE_CHANNEL.replace('@','')}")],
                    [InlineKeyboardButton("👤 Owner", url=f"https://t.me/{OWNER_USERNAME.replace('@','')}")]
                ]
                await update.message.reply_text(
                    "❌ আগে আমাদের Channel Join করো তারপর বট ব্যবহার করতে পারবে 👇",
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
        except Exception:
            await update.message.reply_text("⚠️ Channel check করতে সমস্যা হচ্ছে, পরে চেষ্টা করো।")
            return

    # If joined
    buttons = [
        [InlineKeyboardButton("👤 Owner", url=f"https://t.me/{OWNER_USERNAME.replace('@','')}")]
    ]
    await update.message.reply_text(
        f"👋 Hello {user.first_name}!\n\n✅ তুমি সফলভাবে bot ব্যবহার করতে পারো।",
        reply_markup=InlineKeyboardMarkup(buttons)
    )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 Bot started")
    app.run_polling()


if __name__ == "__main__":
    main()

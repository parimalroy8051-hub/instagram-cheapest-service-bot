from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# ================== CHANGE THESE ==================
BOT_TOKEN = "8188938308:AAEaf7geyzXdnsBVDOmlAYQdSYOXCwuoruA"
FORCE_CHANNEL = "@onlyearnfreee"   # @ সহ
OWNER_USERNAME = "@DigitalTricks_Support"
# =================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    try:
        member = await context.bot.get_chat_member(FORCE_CHANNEL, user_id)
        if member.status not in ["member", "administrator", "creator"]:
            raise Exception("Not joined")
    except:
        keyboard = [
            [InlineKeyboardButton("📌 Join Channel", url=f"https://t.me/{FORCE_CHANNEL.replace('@','')}")],
            [InlineKeyboardButton("✅ Verify", callback_data="verify")]
        ]
        await update.message.reply_text(
            "Welcome 😊\nআগে channel join করো 👇",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    await main_menu(update, context)

async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id

    try:
        member = await context.bot.get_chat_member(FORCE_CHANNEL, user_id)
        if member.status not in ["member", "administrator", "creator"]:
            await query.answer("❌ আগে channel join করো", show_alert=True)
            return
    except:
        await query.answer("❌ আগে channel join করো", show_alert=True)
        return

    await query.message.delete()
    await main_menu(query, context)

async def main_menu(update_or_query, context):
    keyboard = [
        [InlineKeyboardButton("📌 About Bot", callback_data="about")],
        [InlineKeyboardButton("🆘 Help", callback_data="help")],
        [InlineKeyboardButton("👤 Owner", callback_data="owner")]
    ]
    text = "✅ Verification Successful!\nএকটা option select করো 👇"

    if isinstance(update_or_query, Update):
        await update_or_query.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        await update_or_query.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data

    if data == "about":
        await query.answer()
        await query.message.reply_text("🤖 এটা একটা fully custom Telegram bot")
    elif data == "help":
        await query.answer()
        await query.message.reply_text("🆘 Help লাগলে Owner এর সাথে contact করো")
    elif data == "owner":
        await query.answer()
        await query.message.reply_text(f"👤 Owner: {OWNER_USERNAME}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(verify, pattern="verify"))
    app.add_handler(CallbackQueryHandler(buttons))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

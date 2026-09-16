import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = "8965323255:AAGvz92nrEPe6TTewryY3bjBjmOEYqmxdRM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    welcome_text = (
        f"Welcome *{user.first_name}* to *Apex Sheets*! 🚀\n\n"
        "Your ultimate digital store for professional templates and sheets.\n"
        "Price: *$5.00 USDT*\n\n"
        "Click the button below to buy your digital product securely."
    )
    
    keyboard = [
        [InlineKeyboardButton("💳 Buy Apex Sheets ($5 USDT)", callback_data="buy_product")],
        [InlineKeyboardButton("ℹ️ How it Works", callback_data="help_info")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(welcome_text, parse_mode="Markdown", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    if query.data == "buy_product":
        payment_text = (
            "🛒 *Checkout - Apex Sheets*\n\n"
            "Price: `$5.00 USDT`\n\n"
            "To complete your purchase, please send USDT (TRC20 network) to our official wallet address below:\n\n"
            "`TYourUSDTWalletAddressHere123456789`\n\n"
            "After sending the payment, please send the transaction hash (TxID) or a screenshot here, and our team will deliver your file immediately!"
        )
        await query.edit_message_text(text=payment_text, parse_mode="Markdown")
        
    elif query.data == "help_info":
        help_text = (
            "💡 *How Apex Sheets Works:*\n\n"
            "1. Click the Buy button.\n"
            "2. Transfer $5.00 USDT (TRC20).\n"
            "3. Send proof of payment to receive your instant digital download link.\n\n"
            "For support, contact admin."
        )
        await query.edit_message_text(text=help_text, parse_mode="Markdown")

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    print("Bot is starting up...")
    application.run_polling()

if __name__ == "__main__":
    main()
  

import os
import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from datetime import datetime, time

# Telegram bot token
TOKEN = '6138162178:AAFUN8qIyLuq8iAiCQYfSQ5KodxpPUF-NlA'

# Chat ID of the Admin
ADMIN_CHAT_ID = '5016528260'

# Logging configuration
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Initialize the Telegram bot
bot = telegram.Bot(token=TOKEN)


# Define the start command for users
def start(update, context):
    user = update.message.from_user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello {user.first_name}, welcome to the bot!")


# Define the morning message command for the Admin
def morning_message(context):
    context.bot.send_message(chat_id=ADMIN_CHAT_ID, text="Hello, good morning!")


# Define the main function to start the bot
def main():
    # Create the Updater and pass in the bot's token
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the start command for users
    dp.add_handler(CommandHandler("start", start))

    # Start the morning message scheduler for the Admin
    job_queue = updater.job_queue
    job_queue.run_daily(morning_message, time(hour=8, minute=0, second=0))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process is stopped
    updater.idle()


if __name__ == '__main__':
    main()

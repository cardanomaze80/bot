#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.constants import ParseMode
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

  

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""

    # Extract the user's first name. You can also use user.full_name or user.username
    user = update.effective_user
    # username = user.first_name if user.first_name else user.username or "there"
    username = user.username if user.username else user.first_name  or "there"

    # Send a greeting message with the user's name and a description
    greeting_message = f"Hello, {username}! 👋 Welcome to our bot!"
    description = "Here's what you can do here:"
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text=f"{greeting_message}\n\n{description}",
                                   parse_mode=ParseMode.MARKDOWN)

    # Send an image. Replace 'https://example.com/your_photo.jpg' with the actual URL of your image
    # photo_url = "https://cdmcrypto.netlify.app/cdnimg"
    # await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url)


    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data="1"),
            InlineKeyboardButton("Option 2", callback_data="2"),
        ],
        [
            # Replace 'https://your_mini_app_url.com' with the actual URL of your Mini App
            InlineKeyboardButton("Open Mini App", web_app=WebAppInfo(url="https://cdmcrypto.netlify.app")),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the inline keyboard in a new message
    # await update.message.reply_text("Please choose:", reply_markup=reply_markup)
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text="Please choose an option:", 
                                   reply_markup=reply_markup)







async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    await query.edit_message_text(text=f"Selected option: {query.data}")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.

    TOKEN = '6637720245:AAGLltaPLybSJxuXWkZDthbN92TSOLwQUvA'
    print("Running Main")
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()






# # myproject/telegrambot/bot.py
# print("telegram script running")
# from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
# from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters

# async def start(update: Update, context) -> None:
#     await update.message.reply_text('Welcome! What would you like to do today?')

# async def mine(update: Update, context) -> None:
#     keyboard = [
#         [InlineKeyboardButton("Open Web App", url="https://cdmcrypto.netlify.app")],
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await update.message.reply_text('Click the button below to open the web app:', reply_markup=reply_markup)

# async def help_command(update: Update, context) -> None:
#     await update.message.reply_text('Help!')

# async def handle_message(update: Update, context) -> None:
#     text = update.message.text.lower()
#     await update.message.reply_text(f'You said: {text}')

# async def error(update: Update, context) -> None:
#     print(f"Update {update} caused error {context.error}")

# def main():
#     TOKEN = '6637720245:AAGLltaPLybSJxuXWkZDthbN92TSOLwQUvA'
#     print("Running Main")


#     # Use Application.builder() to create a new Application instance
#     application = Application.builder().token(TOKEN).build()
    
#     # Use application.add_handler() to add handlers
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(CommandHandler("mine", mine))
#     application.add_handler(CommandHandler("help", help_command))
#     application.add_handler(MessageHandler(filters.TEXT, handle_message))

#     # Use application.run_polling() to start the bot
#     application.run_polling()

# if __name__ == '__main__':
#     main()
#     print("Running if statement")


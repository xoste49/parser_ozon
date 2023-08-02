import asyncio
import logging

from aiogram import Bot, Dispatcher

from server.settings.components import config

API_TOKEN = config('TELEGRAM_BOT_TOKEN')
USER_ID = config('TELEGRAM_USER_ID')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def __send_message(message: str):
    await bot.send_message(USER_ID, message)


def send_notification_tg(message: str):
    asyncio.run(__send_message(message))

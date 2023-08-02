import asyncio

from server.apps.telegram.bot import TelegramBot


def send_notification_tg(message: str):
    asyncio.run(TelegramBot().send_message(message))

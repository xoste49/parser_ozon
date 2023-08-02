from aiogram import Bot, Dispatcher, types
from server.apps.parser.models import ProductsModel, SessionParsingModel
from server.settings.components import config

API_TOKEN = config('TELEGRAM_BOT_TOKEN')
USER_ID = config('TELEGRAM_USER_ID')


class TelegramBot:
    # Initialize bot and dispatcher
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot)

    @staticmethod
    @dp.message_handler(commands=['products'])
    async def send_products(msg: types.Message):
        session_parsing = await SessionParsingModel.objects.alast()
        products = []
        async for product in ProductsModel.objects.filter(session_parsing=session_parsing):
            products.append(f'{product.id} <a href="https://www.ozon.ru{product.url}">{product.name}</a>')
        await msg.reply('\n'.join(products), parse_mode="HTML")

    async def send_message(self, message: str):
        await self.bot.send_message(USER_ID, message)

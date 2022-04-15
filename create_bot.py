from aiogram import Bot, Dispatcher
from data.telegram_data_pass import get_currency_info_bot2_token as token

bot = Bot(token=token)
dp = Dispatcher(bot)
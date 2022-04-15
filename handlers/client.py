import requests
from datetime import datetime
from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import keyboard_menu
from .yobit_info_valuta import menu_valut
from .weather_show import show_weather
from .vote import vote_start


async def show_menu(message: types.Message):
    await message.delete()
    await bot.send_message(message.from_user.id, 'Что вы хотите узнать?', reply_markup=keyboard_menu)


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(show_menu, Text(equals='Вернуться'))
    dp.register_message_handler(show_menu, commands=['menu', 'start'])
    dp.register_message_handler(menu_valut, Text(equals='Курс'))
    dp.register_message_handler(show_weather, Text(equals='Погода'))
    dp.register_message_handler(vote_start, commands='vote')




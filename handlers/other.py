import string
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from data.check_mat import mat_list
from create_bot import dp
from handlers.yobit_info_valuta import get_data_pairs
from handlers.weather_show import weather
from handlers.vote import vote
from handlers.client import show_menu

#@dp.message_handler()
async def check_message(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
            .intersection(mat_list):
        await message.reply('Давай без мата...')
        await message.delete()

    elif message.text in ['BTC_USD', 'BTC_RUR', 'USD_RUR']:
        return await message.answer(get_data_pairs(pairs=message.text.lower()))

    return await message.answer(weather(message.text.title()))

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(check_message)
    dp.register_callback_query_handler(vote, Text(startswith='like_'))

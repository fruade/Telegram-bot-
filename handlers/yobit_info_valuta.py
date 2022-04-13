import requests
from datetime import datetime
from aiogram import types
from TelegramBot.create_bot import bot

def get_data_pairs(pairs='BTC_USD'):
    pairs = pairs.lower()
    responce = requests.get(url=f'https://yobit.net/api/3/ticker/{pairs}')
    data_json = responce.json()[f"{pairs}"]
    sell_price = round(data_json['sell'], 2)
    return f"{datetime.now().strftime('%d.%m.%Y %H:%M')}\nSell {pairs.split('_')[0].upper()} price: {sell_price:,}\
 {pairs.split('_')[1].upper()}"


async def menu_valut(message: types.Message):
    start_buttons = ['BTC_USD', 'BTC_RUR', 'USD_RUR']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    keyboard.row('Вернуться')
    return await bot.send_message(message.from_user.id, 'Выберите валютную пару', reply_markup=keyboard)







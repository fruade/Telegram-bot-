import requests
from aiogram import types
from TelegramBot.create_bot import bot

def weather(city):
    params = {
        "q": city,
        "units": "metric",
        "appid": "99f3912c416971b7061abe92a247691f"
    }

    url = f'https://api.openweathermap.org/data/2.5/weather?'

    r = requests.get(url=url, params=params).json()
    return f'Температура в городе {city}: {round(int(r["main"]["temp"]))}\u00B0, \nПо ощущениям {round(int(r["main"]["feels_like"]))}\u00B0, \n\
Скорость ветра {r["wind"]["speed"]} м/с, \nВлажность {r["main"]["humidity"]}%'


async def show_weather(message: types.Message):
    start_buttons = ['Тюмень', 'Нягань', 'Прага']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    keyboard.row('Вернуться')
    await bot.send_message(message.from_user.id, 'В каком городе узнать погоду?', reply_markup=keyboard)










from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

data_button = ['Курс', 'Погода']

keyboard_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_menu.add(*data_button)
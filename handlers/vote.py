from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from create_bot import dp
from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher



btn_like = InlineKeyboardButton(text='Нравится', callback_data='like_1')
btn_dislike = InlineKeyboardButton(text='Не нравится', callback_data='like_-1')
keyboard_vote = InlineKeyboardMarkup(row_width=1)
keyboard_vote.add(btn_like, btn_dislike)

data_vote = {}

#@dp.message_handler(commands='vote')
async def vote_start(message: types.Message):
    await message.answer('Как вам бот?', reply_markup=keyboard_vote)


#@dp.callback_query_handler(Text(startswith='like_'))
async def vote(callback: types.CallbackQuery):
    res = int(callback.data.split('_')[1])
    if callback.from_user.id not in data_vote:
        data_vote[callback.from_user.id] = res
        return await callback.answer('Вы проголосовали')
    else:
        return await callback.answer('Вы уже голосовали', show_alert=True)

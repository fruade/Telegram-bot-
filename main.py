# -*- coding: utf-8 -*-
from aiogram import executor
from create_bot import dp
from handlers import client, other

async def on_start_up(_):
    print('Бот запущен...')


client.register_handler_client(dp)
other.register_handlers_other(dp)


def main():
    executor.start_polling(dp, skip_updates=True, on_startup=on_start_up)


if __name__ == '__main__':
    main()
import logging
from create_bot import dp
from aiogram import executor

logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
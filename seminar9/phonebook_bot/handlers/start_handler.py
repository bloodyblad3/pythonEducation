from aiogram import Dispatcher, types

async def help(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(help, commands=['start', 'help'])
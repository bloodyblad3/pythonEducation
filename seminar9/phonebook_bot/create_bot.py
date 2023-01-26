import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage 

load_dotenv()

storage = MemoryStorage()
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher(bot, storage=storage)
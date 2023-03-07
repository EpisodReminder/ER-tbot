from aiogram import Bot, Dispatcher
from language_manager import language_manager
from aiogram.contrib.fsm_storage.memory import MemoryStorage

with open("key.txt") as file:
    KEY = file.read()
bot = Bot(KEY)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
loc = language_manager.LanguageManager()

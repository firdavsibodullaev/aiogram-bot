from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

token: str = config.BOT_TOKEN
parse_mode: str = types.ParseMode.HTML

bot = Bot(token=token, parse_mode=parse_mode)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

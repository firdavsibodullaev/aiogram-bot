import re
from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils.deep_linking import get_start_link

from filters import IsPrivate
from loader import dp


@dp.message_handler(CommandStart(deep_link="private"), IsPrivate())
async def private_chat(message: types.Message):
    await message.answer(f"Bu {message.get_args()} chat")


@dp.message_handler(CommandStart(deep_link="Text"))
async def bot_start(message: types.Message):
    await message.answer("Startni bosding, va Text argumentini jo'natding")


@dp.message_handler(CommandStart(deep_link=re.compile(r"^[A-Za-z0-9_-]{3,15}$")))
async def bot_deep_link_regex(message: types.Message):
    args = message.get_args()
    await message.reply(text=f"Argument jo'natding <strong>{args}</strong>")


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    args = message.get_args()
    if args == '':
        deep_link = await get_start_link(payload="Test")
        await message.answer(text="Startni bosding, argumentsiz")
        await message.answer(text=f"Sening linking, {deep_link}")
    else:
        await message.answer(f"Startni bosding, va {args} argumentini jo'natding")

from loader import dp, bot

from aiogram import types


@dp.message_handler(text="/start")
async def bot_start(message: types.Message):
    first_name: str = message.chat.first_name
    text: str = f"Hello mr. {first_name}"
    await message.answer(text=text)


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def bot_photo(message: types.Message):
    file_id: str = message.photo[-1].file_id
    await message.answer_photo(photo=file_id)


@dp.message_handler()
async def bot_echo(message: types.Message):
    chat_id: int = message.chat.id
    text: str = message.text
    await bot.send_message(chat_id=chat_id, text=text)
    await message.reply(text=text)
    await message.answer(text=text, reply=True)

import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import start_kb
from googletrans import Translator

TELEGRAM_API_TOKEN = '7624657726:AAFS2ceg9Mfcqh9Vgp2uh25toj3f9os56o0'

bot = Bot(token=TELEGRAM_API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

logging.basicConfig(level=logging.INFO)

class TranslateState(StatesGroup):
    til = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Salom tarjimon botiga xush kelibsiz! Kerakli tilni tanlang:", reply_markup=start_kb)

@dp.callback_query_handler()
async def tilni_tanlash(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'uz_ru':
        await state.update_data(til='uz_ru')
        await bot.send_message(chat_id=call.from_user.id, text="Siz o'zbekchadan ruschaga tanladingiz\nNimani tarjima qilish kerak?")
    elif call.data == 'ru_uz':
        await state.update_data(til='ru_uz')
        await bot.send_message(chat_id=call.from_user.id, text="Вы выбрали с русского на узбекский\nЧто переводить?")
    elif call.data == 'en_uz':
        await state.update_data(til='en_uz')
        await bot.send_message(chat_id=call.from_user.id, text="You have selected from English to Uzbek\nWhat should be translated?")
    elif call.data == 'uz_en':
        await state.update_data(til='uz_en')
        await bot.send_message(chat_id=call.from_user.id, text="Siz o'zbekchadan inglisga tanladingiz\nNimani tarjima qilish kerak?")
    elif call.data == 'en_ru':
        await state.update_data(til='en_ru')
        await bot.send_message(chat_id=call.from_user.id, text="You have selected from English to Russian\nWhat should be translated?")
    elif call.data == 'ru_en':
        await state.update_data(til='ru_en')
        await bot.send_message(chat_id=call.from_user.id, text="Вы выбрали с русского на английский\nЧто переводить?")

@dp.message_handler()
async def tarjima(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    til = user_data.get('til')
    user_text = message.text
    if til:
        tildan, tilga = til.split('_')
        tarjimon = Translator()
        translated_text = tarjimon.translate(text=user_text, dest=tilga, src=tildan)
        await message.answer(f"Siz so'ragan matn:\n{user_text}\n\nTarjimasi:\n{translated_text.text}")
    else:
        await message.answer("Iltimos, tarjima qilish tilini tanlang.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

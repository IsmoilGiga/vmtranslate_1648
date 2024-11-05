from aiogram import types

start_kb = types.InlineKeyboardMarkup(inline_keyboard=[
    [types.InlineKeyboardButton("🇺🇿 ▶️ 🇷🇺", callback_data='uz_ru'), types.InlineKeyboardButton("🇷🇺 ▶️ 🇺🇿", callback_data='ru_uz')],
    [types.InlineKeyboardButton("🇺🇸 ▶️ 🇺🇿", callback_data='en_uz'), types.InlineKeyboardButton("🇺🇿 ▶️ 🇺🇸", callback_data='uz_en')],
    [types.InlineKeyboardButton("🇺🇸󠁧󠁢 ▶️ 🇷🇺", callback_data='en_ru'), types.InlineKeyboardButton("🇷🇺 ▶️ 🇺🇸", callback_data='ru_en')]
])

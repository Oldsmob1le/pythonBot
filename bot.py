import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Получаем токен из переменной окружения
API_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Создаем Inline-кнопку с WebAppInfo
    web_app = WebAppInfo(url='https://<your_domain>')
    inline_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("Перейти", web_app=web_app))
    
    await message.answer("Нажмите на кнопку ниже, чтобы перейти к веб-приложению.", reply_markup=inline_kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
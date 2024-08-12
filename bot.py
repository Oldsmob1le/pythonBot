from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import Command
from aiogram import F
import logging
import os
import asyncio

API_TOKEN = os.getenv('BOT_TOKEN')  # Получаем токен из переменной окружения

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    # Создаем Inline-кнопку с WebAppInfo
    web_app = WebAppInfo(url='https://abdulin.vercel.app')
    inline_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("Перейти", web_app=web_app))
    
    await message.answer("Нажмите на кнопку ниже, чтобы перейти к веб-приложению.", reply_markup=inline_kb)

async def on_startup(dispatcher: Dispatcher):
    logging.info("Starting bot...")

async def main():
    # Запуск бота
    await dp.start_polling(bot, on_startup=on_startup)

if __name__ == '__main__':
    asyncio.run(main())
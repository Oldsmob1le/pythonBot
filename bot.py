from aiogram import Bot, Dispatcher, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils import executor
import logging
import os

API_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

@dp.message(F.command("start"))
async def send_welcome(message):
    # Создаем Inline-кнопку с WebAppInfo
    web_app = WebAppInfo(url='https://<your_domain>')
    inline_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("Перейти", web_app=web_app))
    
    await message.answer("Нажмите на кнопку ниже, чтобы перейти к веб-приложению.", reply_markup=inline_kb)

async def on_startup(dispatcher):
    logging.info("Starting bot...")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, on_startup=on_startup)

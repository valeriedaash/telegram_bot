import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command

# Инициализация объектов
TOKEN = os.getenv('TOKEN') 
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(
    level=logging.INFO, 
    filename = 'bot_log.log', 
    format = "%(asctime)s - %(levelname)s - %(message)s"
    )

# Обработка команды start
@dp.message(Command(commands=['start']))
async def process_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}!'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id = user_id, text = text)

# Обработка всех сообщений
@dp.message()
async def process_message(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    transliteration = {
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Д': 'D',
        'Е': 'E',
        'Ё': 'E',
        'Ж': 'ZH',
        'З': 'Z',
        'И': 'I',
        'Й': 'I',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'KH',
        'Ц': 'TS',
        'Ч': 'CH',
        'Ш': 'SH',
        'Щ': 'SHCH',
        'Ы': 'Y',
        'Ъ': 'IE',
        'Э': 'E',
        'Ю': 'IU',
        'Я': 'IA',
        ' ': ' '
    }
    bot_answer = ''
    for i in text.upper():
        bot_answer += transliteration.get(i, i)
        bot_answer = bot_answer.title()
    logging.info(f'{user_name} {user_id}: {text}')
    await message.answer(bot_answer)

# Запуск процесса пуллинга
if __name__ == '__main__':
    dp.run_polling(bot)


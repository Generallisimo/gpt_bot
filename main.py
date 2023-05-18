import random
import asyncio

import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = '6086537588:AAHH75q1QhJfSSL553v7qH_SvQYgV69dhUQ'

openai.api_key = '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'

sticker_name = 'Patrick_Bateman'

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Задавай чертовы вопросы🫥, но хакать я не буду😈\n\n© Fscoiety☠️")

@dp.message_handler()
async def send(message: types.Message):
    
    sticker_set = await bot.get_sticker_set(sticker_name)
    stickers = sticker_set.stickers
    random_stick = random.choice(stickers)
    
    sticker_message = await message.answer_sticker(random_stick.file_id)
    
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= message.text,
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=["You:"]
    )

    await message.answer(response['choices'][0]['text'])
    
    await bot.delete_message(message.chat.id, sticker_message.message_id)
    
executor.start_polling(dp, skip_updates=True)
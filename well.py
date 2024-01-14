import asyncio
import random
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.enums import DiceEmoji

bot = Bot('6924718093:AAG_5AvFdn_6TnzZrzulTk96n5e6c_yp11s')
dp = Dispatcher()


@dp.message(F.text == '/start')
async def start_message(message: Message):
    print(message)
    await message.answer(f'Welcome to the First bot {message.from_user.first_name}')


@dp.message(Command(commands=['random_numbers', 'random']))
async def random_numbers(message: Message, command: CommandObject):
    a, b = [int(n) for n in command.args.split('-')]
    rnum = random.randint(a, b)
    await message.reply(f'Random numbers {rnum}')


@dp.message(F.text == 'play')
async def play_game(message: Message):
    x = await message.answer_dice(DiceEmoji.DICE)
    print(x.dice.value)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
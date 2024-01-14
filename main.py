# #syncronous
# def task1():
#     print('Task 1')
#
# def task2():
#     print('Task 2')
#
# def main():
#     task1()
#     task2()
#
# if __name__ == '__main__':
#     main()

# #asyncronous
# import asyncio
# async def task1():
#     await asyncio.sleep(1)
#     print('Task1')
#
# async def task2():
#     await asyncio.sleep(1)
#     print('Task2')
#
# async def main():
#     task1_1 = asyncio.create_task(task1())
#     task1_2 = asyncio.create_task(task2())
#
#     await task1_1
#     await task1_2
#
# if __name__ == '__main__':
#     asyncio.run(main())

# #multithreading
# import time
# import threading
#
# def generate_numbers():
#     for i in range(30, 40):
#         time.sleep(0.5)
#         print(i)
#
# def generate_letters():
#     for i in 'XYZ':
#         time.sleep(0.5)
#         print(i)
#
# thread1 = threading.Thread(target=generate_letters)
# thread2 = threading.Thread(target=generate_numbers)
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()

# #bot
# import asyncio
# import random
# from aiogram import Bot, Dispatcher, F
# from aiogram.types import Message
# from aiogram.filters import Command, CommandObject
# from aiogram.enums.dice_emoji import DiceEmoji
#
# bot = Bot(token='6924718093:AAG_5AvFdn_6TnzZrzulTk96n5e6c_yp11s')
# dp = Dispatcher()
#
#
# @dp.message(Command(commands=['start']))
# async def start(message: Message):
#     await message.answer('There are 3 commands in our bot called: /start, /help and /aboutus')
#
#
# @dp.message(Command(commands=['help']))
# async def help(message: Message):
#     await message.answer('You clicked a command help')
#
#
# @dp.message(Command(commands=['about us']))
# async def about_us(message: Message):
#     await message.answer('It happened a long time ago...')
#
#
# @dp.message(F.text == '/game')
# async def game(message: Message):
#     await message.answer_dice(DiceEmoji.BASKETBALL)
#     print(message.dice.value)
#
#
# @dp.message(Command(commands=['random_numbers', 'random']))
# async def random_numbers(message: Message, command: CommandObject):
#     a, b = [int(n) for n in command.args.split('-')]
#     rnum = random.randint(a, b)
#     await message.reply(f'Random numbers {rnum}')
#
#
# async def main():
#     await bot.delete_webhook(drop_pending_updates=True)
#     await dp.start_polling(bot)
#
# asyncio.run(main())





from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import WebAppInfo

bot = Bot(token='6143802430:AAHMopnnKkgFhn1XwgMHIn1i-_9YbLC283U')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add(types.KeyboardButton('Order food', web_app=types.WebAppInfo(url='https://www.google.com')))
	await message.reply('Hello! Welcome to Bad Omen!', reply_markup=markup)

@dp.message_handler()
async def echo(message: types.Message):
	await message.answer(message.text)
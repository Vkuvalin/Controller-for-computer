import json, string
from aiogram.types import Message
from aiogram import Dispatcher
from create_bot import dp, bot
from config import admin_id


'''***********************************ОСНОВНАЯ ЧАСТЬ*********************************************************'''
'''**********************************************************************************************************'''


'''***********************************СЛУЖЕБНАЯ ЧАСТЬ/ПОДВАЛ*************************************************'''
async def echo_send(message: Message):
    # Фильтер для мата
    if ({i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))) != set()):
        await message.reply('Мат запрещен!')
        await message.delete()
'''***********************************************************************************************************'''

'''***********************************ЗАПУСК ФУНКЦИЙ**********************************************************'''
def register_message_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)  # Вот эта хрень, вроде как, должна быть всегда в самом низу.
'''***********************************************************************************************************'''
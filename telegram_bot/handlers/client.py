from aiogram.types import Message, ReplyKeyboardRemove, KeyboardButton,\
    ReplyKeyboardMarkup, InputTextMessageContent, InlineQueryResultArticle, InlineQuery
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
import asyncio

# Локальные импорты
# from data_base import sqlite_db, open_db_file
from config import admin_id
from create_bot import dp, bot
from keyboards import kb_client, kb_ksu_С, kb_ksu_R, kb_son, \
    kb_browser, kb_music, kb_music1, ksu_sites, kb_sc, kb_video, kb_video1, kb_mouse

# Для "Ксю"
# from random import *
import datetime
# import radar

# Браузер
import webbrowser

# Выключение
import subprocess
import sys
import os
from subprocess import Popen

# Скрин
import pyautogui
import cv2

# Клавиатура/мышь
import keyboard
# from pynput.keyboard import Key, Controller
# from pynput.mouse import Button, Controller

# mouse = Controller()
# kb = Controller()
#
# def press(button):
#     kb.press(button)
#     kb.release(button)









# Доводя до идеала типа можно написать кучу проверок, чтобы работало на "ура!", но это когда-то потом
# А может для красоты и емкости сделать рили пульты хотя бы через инлайн кнопки?
# Замечание убрать
"""
    else:
        await message.reply('Ошибка. Воспользуйся кнопками.')
        await Ksu_search.browser4.set()  <----- вот эту хуйню
        return None

"""


'''***********************************ОБЩИЙ******************************************************************'''
'''*********************ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ*************************'''
chat_count = 0
'''*******************************************************************'''
'''**********************************************************************************************************'''

'''***********************************ОСНОВНАЯ ЧАСТЬ*********************************************************'''
# Стартовые команды
async def startRun(message: Message):
    try:
        if message.text[1:] == 'start':
            await bot.send_message(message.from_user.id, 'Приветствую тебя, мой друг!', reply_markup=kb_client)
            await message.delete()
            await bot.send_message(message.from_user.id, 'Советую посетить "/help" - там ты узнаешь все мои команды!')

        if message.text[1:] == 'help':                                                                                  # Подумаю, может что-нибудь сделаю с этим
            await bot.send_message(message.from_user.id, 'Да мне бы кто помог...')
            await asyncio.sleep(2)  # Типа создает задержку! Офигенная функция
            await bot.send_message(message.from_user.id, 'Ладно-ладно... Сейчас что-нибудь придумаю.')
            await asyncio.sleep(2)
            await bot.send_message(message.from_user.id, 'Хм...')
    except:
        await message.reply('Бот не может ответить - необходимо добавиться к нему: \n@Multi_vlad_bot')


# Отключение клавиатуры ("отключить_клавиатуру")
async def keyboardRemove(message: Message):
    await bot.send_message(message.from_user.id, 'Пока-пока', reply_markup=ReplyKeyboardRemove())
    await bot.send_message(message.from_user.id, 'Если снова понадоблюсь, напиши "/start"')



'''*********************ФОРМА-(Ксю)*************************'''
class Ksu_search(StatesGroup):
    choice = State()

    browser = State()
    browser2 = State()
    browser3 = State()
    browser4 = State()
    video = State()

    sleep = State()
    sleep2 = State()
    apps = State()
    reader = State()
    sites = State()
    screenshot = State()
    mouse = State()


# Начало диалога загрузки.
async def ksu(message: Message):
    if message.from_user.id == admin_id or message.from_user.username == "Steppz":
        await Ksu_search.choice.set()
        await message.answer('Выбери режим: ', reply_markup=kb_ksu_С)
    else:
        await message.answer('Упс, прости, но доступ запрещен.')


# 0 - Основное меню
async def load_choice(message: Message):

    if message.text == 'Браузер':
        await Ksu_search.browser.set()
        await message.answer('Что делаем?', reply_markup=kb_browser)

    elif message.text == 'Сон/Выкл':
        await Ksu_search.sleep.set()
        await message.answer('Что делаем?', reply_markup=kb_son)

    elif message.text == 'Приложения':
        await Ksu_search.apps.set()
        await message.answer('Что делаем?', reply_markup=kb_ksu_R)

    elif message.text == 'Скриншот':
        await Ksu_search.screenshot.set()
        await message.answer('Кого будем снимать?', reply_markup=kb_sc)

    elif message.text == 'Сообщение':
        await Ksu_search.reader.set()
        await message.answer('Если захочешь выйти, просто напиши "стоп".', reply_markup=ReplyKeyboardRemove())
        await message.answer('Введи текст:')

    elif message.text == 'Мышь':
        await Ksu_search.mouse.set()
        await message.answer('Мышь подключена', reply_markup=kb_mouse)
    else:
        await message.answer('Ой, а я таких слов не знаю. Воспользуйся, пожалуйста, кнопками.')


# Функция выхода из состояния ("Отмена")
async def cancel_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("Ничего страшного", reply_markup=kb_client)


'''++++++++++++++++++Браузер+++++++++++++++++++++'''
# 1 - Браузер
async def open_browser(text):
    webbrowser.open(text)

async def load_browser(message: Message, state: FSMContext):

    if message.text == 'Открыть ссылку':
        await Ksu_search.browser2.set()
        await message.answer("Отправь ссылку: ", reply_markup=ReplyKeyboardRemove())
    elif message.text == 'Сохранить ссылку':
        await Ksu_search.browser3.set()
        await message.answer("Отправь ссылку: ", reply_markup=ReplyKeyboardRemove())

    elif message.text == "Музыка":
        await Ksu_search.browser4.set()
        await message.answer("Кайф", reply_markup=kb_music)

    elif message.text == "Видео":
        await Ksu_search.video.set()
        await message.answer("Кайф", reply_markup=kb_video)

    elif message.text == 'Назад':
        await ksu(message)
        return None
    elif message.text == 'Пожалуй, пойду':
        await state.finish()
        await message.answer("Пока-пока!", reply_markup=kb_client)
        return None
    else:
        await message.reply('Ошибка. Воспользуйся кнопками.')
        await Ksu_search.browser.set()
        return None

async def load_browser2(message: Message):
    await open_browser(message.text)

    await message.answer("Выполнено.", reply_markup=kb_browser)
    await Ksu_search.browser.set()
    return None

async def load_browser3(message: Message):
    fin = open("archive.txt", "a")
    fin.write('\n'+message.text)
    fin.close()

    await message.answer("Сохранил", reply_markup=kb_browser)
    await Ksu_search.browser.set()
    return None

async def load_browser4(message: Message):
    if message.text == '+':
        keyboard.send("volume up")
    elif message.text == '<':
        keyboard.send("previous track")
    elif message.text == '||':
        keyboard.send("play/pause media")
        await message.answer('||', reply_markup=kb_music1)
    elif message.text == 'O':
        keyboard.send("play/pause media")
        await message.answer('O', reply_markup=kb_music)
    elif message.text == '>':
        keyboard.send("next track")
    elif message.text == '-':
        keyboard.send("volume down")
    elif message.text == 'Назад':
        await Ksu_search.browser.set()
        await message.answer('Что делаем?', reply_markup=kb_browser)
        return None
    elif message.text == 'Сайт':
        await Ksu_search.sites.set()
        await message.answer("Ну-ка, что у нас тут?", reply_markup=ksu_sites)
        return None
    else:
        await message.reply('Ошибка. Воспользуйся кнопками.')
        await Ksu_search.browser4.set()
        return None

async def load_sites(message: Message):
    if message.text == 'VK':
        webbrowser.open('https://vk.com/audios144901827')
        await Ksu_search.browser4.set()
        await message.answer("Готово", reply_markup=kb_music)
    elif message.text == 'Яндекс.Музыка':
        webbrowser.open('https://music.yandex.ru/home')
        await Ksu_search.browser4.set()
        await message.answer("Готово", reply_markup=kb_music)
    elif message.text == 'Назад':
        await Ksu_search.browser4.set()
        await message.answer("Ой", reply_markup=kb_music)
    else:
        await message.reply('Ошибка. Воспользуйся кнопками.')
        await Ksu_search.browser4.set()
        return None

async def load_video(message: Message):
    from pynput.keyboard import Key, Controller
    kb = Controller()

    def press(button):
        kb.press(button)
        kb.release(button)

    if message.text == '+':
        press(Key.up)
    elif message.text == '<':
        press(Key.left)
    elif message.text == '||':
        keyboard.send("spacebar")
        await message.answer('||', reply_markup=kb_video1)
    elif message.text == 'O':
        keyboard.send("spacebar")
        await message.answer('O', reply_markup=kb_video)
    elif message.text == '>':
        press(Key.left)
    elif message.text == '-':
        press(Key.down)
    elif message.text == 'full':
        keyboard.send("f")
    elif message.text == 'Назад':
        await Ksu_search.browser.set()
        await message.answer('Что делаем?', reply_markup=kb_browser)
        return None
    else:
        await message.reply('Ошибка. Воспользуйся кнопками.')
        await Ksu_search.video.set()
        return None

'''++++++++++++++++++Выключение++++++++++++++++++'''
async def sleeping():
    sleeping = subprocess.Popen(["powershell.exe", os.path.abspath('slepping.ps1')], stdout=sys.stdout)
    sleeping.communicate()

# 2 - Выключение-1
async def load_sleep(message: Message, state: FSMContext):

    if message.text == 'Сон':
        await sleeping()
        await bot.send_message(message.from_user.id, 'Выполнено!', reply_markup=kb_ksu_С)
        await Ksu_search.choice.set()
        return None

    elif message.text == 'Сон по таймеру':
        await Ksu_search.sleep2.set()
        await message.answer("Хорошо. Напиши время через сколько произвести выключение в минутах: ", reply_markup=ReplyKeyboardRemove())

    elif message.text == 'Экран':
        Popen(os.path.abspath('screen.bat'))
        return None

    elif message.text == 'Назад':
        await ksu(message)
        return None

    elif message.text == 'Пожалуй, пойду':
        await state.finish()
        await message.answer("Пока-пока!", reply_markup=kb_client)
        return None

    else:
        await message.reply('Ошибка. Воспользуйся кнопками.')
        await Ksu_search.sleep.set()
        return None

# 2.1 - Выключение-2
async def load_sleep2(message: Message):
    time = message.text

    await asyncio.sleep(int(time) * 60)
    await sleeping()

    await bot.send_message(message.from_user.id, 'Выполнено!', reply_markup=kb_ksu_С)
    await Ksu_search.choice.set()
    return None


'''++++++++++++++++++Приложения++++++++++++++++++'''
# 3 - Приложения
async def load_apps(message: Message, state: FSMContext):
    choice = None
    if message.text == 'Одно фото':
        choice = 'Одно фото'
    elif message.text == 'Как повезет':
        choice = 'Как повезет'
    elif message.text == 'Назад':
        await ksu(message)
        return None
    elif message.text == 'Пожалуй, пойду':
        await state.finish()
        await message.answer("Пока-пока!", reply_markup=kb_client)
        return None
    else:
        await message.reply('Ошибка. Воспользуйся кнопками.')
        await Ksu_search.apps.set()
        return None

    await message.answer(choice)
    await Ksu_search.apps.set()
    return None

# 4 - Скриншот
async def load_screenshot(message: Message):
    if message.text == 'Экран':
        pyautogui.screenshot('screenshot/screenshot.png')
        await bot.send_photo(message.from_user.id, photo=open('screenshot/screenshot.png', 'rb'))
        return None
    elif message.text == 'Вебкамера':
        try:
            cap = cv2.VideoCapture(0)  # Включаем первую камеру
            for i in range(30):  # "Прогреваем" камеру, чтобы снимок не был тёмным
                cap.read()
            ret, frame = cap.read()  # Делаем снимок
            cv2.imwrite('screenshot/cam.png', frame)  # Записываем в файл
            cap.release()  # Отключаем камеру

            await bot.send_photo(message.from_user.id, photo=open('screenshot/cam.png', 'rb'))
            return None
        except:
            await message.reply('Камера не подключена :(')
            return None
    elif message.text == 'Назад':
        await ksu(message)
        return None
    else:
        await message.reply('Ошибка. Воспользуйся кнопками.')
        await Ksu_search.apps.set()
        return None


# 5 - Сообщение
async def load_reader(message: Message):
    text = None
    global chat_count

    if message.text.lower() != 'стоп':
        s = os.path.abspath('сhat.txt')
        if chat_count <= 0:
            await message.answer('Введи текст:')
            os.startfile(s)
            fin = open("сhat.txt", "a")
            fin.write('\n' + str(datetime.datetime.now()))
            fin.close()
            chat_count += 1
        text = message.text
        fin = open("сhat.txt", "a")
        fin.write('\n' + text)
        fin.close()

        os.system("TASKKILL /F /IM notepad.exe")

        await Ksu_search.reader.set()
        os.startfile(s)
    else:
        fin = open("сhat.txt", "a")
        fin.write('\n')
        fin.close()
        os.system("TASKKILL /F /IM notepad.exe")
        chat_count = 0
        await Ksu_search.choice.set()
        await message.answer('Выбери режим: ', reply_markup=kb_ksu_С)

# 6 - Мышь
async def load_mouse(message: Message):
    from pynput.mouse import Button, Controller
    mouse = Controller()

    if message.text == '↑':
        mouse.move(0, -10)
    elif message.text == '↑↑':
        mouse.move(0, -100)
    elif message.text == '←':
        mouse.move(-10, 0)
    elif message.text == '←←':
        mouse.move(-100, 0)
    elif message.text == 'Л':
        mouse.press(Button.left)
        mouse.release(Button.left)
    elif message.text == '2Л':
        mouse.click(Button.left, 2)
    elif message.text == 'П':
        mouse.press(Button.right)
        mouse.release(Button.right)
    elif message.text == '→':
        mouse.move(10, 0)
    elif message.text == '→→':
        mouse.move(100, 0)
    elif message.text == '↓':
        mouse.move(0, 10)
    elif message.text == '↓↓':
        mouse.move(0, 100)
    elif message.text == 'up':
        mouse.scroll(0, 5)
    elif message.text == 'down':
        mouse.scroll(0, -5)
    elif message.text == 'Назад':
        await Ksu_search.choice.set()
        await message.answer('Выбери режим: ', reply_markup=kb_ksu_С)
        return None
    else:
        await message.reply('Ошибка. Воспользуйся кнопками.')
        return None



'''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''
'''**********************************************************************************************************'''


'''***********************************ЗАПУСК ФУНКЦИЙ*********************************************************'''
def register_message_client(dp : Dispatcher):
    dp.register_message_handler(startRun, commands=['start', 'help'])
    dp.register_message_handler(keyboardRemove, Text(equals='отключить_клавиатуру', ignore_case=True), state="*")


    '''*********************ФОРМА-(Ксю)*************************'''
    dp.register_message_handler(ksu, Text(equals='Компьютер', ignore_case=True), state="*")

    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")

    dp.register_message_handler(load_choice, state=Ksu_search.choice)

    dp.register_message_handler(load_browser, state=Ksu_search.browser)
    dp.register_message_handler(load_browser2, state=Ksu_search.browser2)
    dp.register_message_handler(load_browser3, state=Ksu_search.browser3)
    dp.register_message_handler(load_browser4, state=Ksu_search.browser4)
    dp.register_message_handler(load_sites, state=Ksu_search.sites)
    dp.register_message_handler(load_video, state=Ksu_search.video)
    dp.register_message_handler(load_sleep, state=Ksu_search.sleep)
    dp.register_message_handler(load_sleep2, state=Ksu_search.sleep2)
    dp.register_message_handler(load_apps, state=Ksu_search.apps)
    dp.register_message_handler(load_reader, state=Ksu_search.reader)
    dp.register_message_handler(load_screenshot, state=Ksu_search.screenshot)
    dp.register_message_handler(load_mouse, state=Ksu_search.mouse)
    '''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''
'''**********************************************************************************************************'''










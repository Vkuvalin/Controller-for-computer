from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

# Анотация к импортам
"""
1. ReplyKeyboardMarkup  - это создание обычной клавиатуры.   Размер - resize_keyboard=True, Сворачивает - one_time_keyboard=True
2. KeyboardButton       - с помощью него создается кнопка.
3. ReplyKeyboardRemove  - короче она типа нужна, чтобы клава удалялась.
"""


# Создание кнопок и именование их
b2 = KeyboardButton('/help')
b3 = KeyboardButton('Компьютер')
b10 = KeyboardButton('отключить_клавиатуру')

# Данные кнопки благодаря второму аргументу будут возвращать отличные от названия сообщения.
# b4 = KeyboardButton('Поделиться номером', request_contact=True)     # Телефон. Скидывает номер юзера (он должен разрешить)
# b5 = KeyboardButton('Отправить где я', request_location=True)       # Телефон. Скидывает геолокацию юзера (он должен разрешить)


# Создаём клавиатуру и заполняем
'''
1. resize_keyboard      - меняет размер кнопок.
2. one_time_keyboard    - сворачивает клавиатуру после выбора.
3. row_width=           - устанавливает кол-во кнопок в одном ряду.
                          не распространяется на метод row
# Для callback кнопок
4. callback_data=       - значение, на которое будет реагировать хендлер (типа команды)
5. show_allert=         - выдает не простро всплывающее, но с подтверждением "ок". До 200 символов
'''
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(b2, b3).add(b10)

# Есть 3 типа добавления:
# add()         - добавляет тупо с новой строки
# insert()      - добавляет справа, если есть место
# row(b1, b2)   - все кнопки в строку
# Плюс ещё можно добавить списком




# Пока не нужно. Не удаляю
"""--------------------------Создание inline клавиатуры--------------------------"""
# Подробная информация в файле inline.py
urlkb = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Ссылка', url='https://youtube.com')
urlButton2 = InlineKeyboardButton(text='Ссылка2', url='https://google.com')

# Также крайне круто, что кнопки можно засунуть в список
x = [InlineKeyboardButton(text='Ссылка2', url='https://google.com'),
     InlineKeyboardButton(text='Ссылка2', url='https://google.com'),
     InlineKeyboardButton(text='Ссылка2', url='https://google.com')]

urlkb.add(urlButton, urlButton2).row(*x)

# Нужно отметить, что ссылки добавляются непосредственно к ответному сообщению
"""
@dp.message_handler(commands='ссылки')
async def url_command(message: types.Message):
    await message.answer('Ссылочки:', reply_markup=urlkb)
"""
"""------------------------------------------------------------------------------"""




# Функционал реализации поиска фотографий для Ксю
# Общий выбор
'''*********************ФОРМА-(Ксю)*************************'''
ksu_С_1 = KeyboardButton('Браузер')
ksu_С_2 = KeyboardButton('Сон/Выкл')
ksu_С_3 = KeyboardButton('Приложения')
ksu_С_4 = KeyboardButton('Скриншот')
ksu_С_5 = KeyboardButton('Сообщение')
ksu_С_10 = KeyboardButton('Отмена')
kb_ksu_С = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ksu_С.row(ksu_С_1, ksu_С_2, ksu_С_3).row(ksu_С_4, ksu_С_5).add(ksu_С_10)


# Скриншот
ksu_R_1 = KeyboardButton('Заблокированно')
ksu_R_2 = KeyboardButton('Заблокированно')
ksu_R_3 = KeyboardButton('Назад')
ksu_R_4 = KeyboardButton('Пожалуй, пойду')
kb_ksu_R = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ksu_R.row(ksu_R_1, ksu_R_2).add(ksu_R_3).insert(ksu_R_4)


# Скриншот
ksu_sc_1 = KeyboardButton('Экран')
ksu_sc_2 = KeyboardButton('Вебкамера')
ksu_sc_3 = KeyboardButton('Назад')
kb_sc = ReplyKeyboardMarkup(resize_keyboard=True)
kb_sc.row(ksu_sc_1, ksu_sc_2).add(ksu_sc_3)


# Браузер
ksu_B_1 = KeyboardButton('Открыть ссылку')
ksu_B_2 = KeyboardButton('Сохранить ссылку')
ksu_B_3 = KeyboardButton('Музыка')
ksu_B_4 = KeyboardButton('Видео')
ksu_B_9 = KeyboardButton('Назад')
ksu_B_10 = KeyboardButton('Пожалуй, пойду')
kb_browser = ReplyKeyboardMarkup(resize_keyboard=True)
kb_browser.row(ksu_B_1, ksu_B_2).row(ksu_B_3, ksu_B_4).add(ksu_B_9, ksu_B_10)

# Браузер_Музыка
ksu_M_1 = KeyboardButton('+')
ksu_M_2 = KeyboardButton('<')
ksu_M_3 = KeyboardButton('||')
ksu_M1_3 = KeyboardButton('O')
ksu_M_4 = KeyboardButton('>')
ksu_M_5 = KeyboardButton('-')
ksu_M_9 = KeyboardButton('Назад')
ksu_M_10 = KeyboardButton('Сайт')
kb_music = ReplyKeyboardMarkup(resize_keyboard=True)
kb_music.add(ksu_M_1).row(ksu_M_2, ksu_M_3, ksu_M_4).add(ksu_M_5).add(ksu_M_9, ksu_M_10)

kb_music1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_music1.add(ksu_M_1).row(ksu_M_2, ksu_M1_3, ksu_M_4).add(ksu_M_5).add(ksu_M_9, ksu_M_10)

# Браузер_Видео
ksu_V_1 = KeyboardButton('+')
ksu_V_2 = KeyboardButton('<')
ksu_V_3 = KeyboardButton('||')
ksu_V1_3 = KeyboardButton('O')
ksu_V_4 = KeyboardButton('>')
ksu_V_5 = KeyboardButton('-')
ksu_V_6 = KeyboardButton('full')
ksu_V_9 = KeyboardButton('Назад')
kb_video = ReplyKeyboardMarkup(resize_keyboard=True)
kb_video.add(ksu_V_1).row(ksu_V_2, ksu_V_3, ksu_V_4).add(ksu_V_5).add(ksu_V_6).add(ksu_V_9)

kb_video1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_video1.add(ksu_V_1).row(ksu_V_2, ksu_V1_3, ksu_V_4).add(ksu_V_5).add(ksu_V_6).add(ksu_M_9)

# Браузер_Музыка_Сайт
ksu_site_1 = KeyboardButton('VK')
ksu_site_2 = KeyboardButton('Яндекс.Музыка')
ksu_site_3 = KeyboardButton('Назад')
ksu_sites = ReplyKeyboardMarkup(resize_keyboard=True)
ksu_sites.row(ksu_site_1, ksu_site_2).add(ksu_site_3)


# Сон/Выкл
ksu_s_1 = KeyboardButton('Сон')
ksu_s_2 = KeyboardButton('Сон по таймеру')
ksu_s_3 = KeyboardButton('Экран')
ksu_s_9 = KeyboardButton('Назад')
ksu_s_10 = KeyboardButton('Пожалуй, пойду')
kb_son = ReplyKeyboardMarkup(resize_keyboard=True)
kb_son.row(ksu_s_1, ksu_s_2, ksu_s_3).add(ksu_s_9).insert(ksu_s_10)
'''*********************************************************'''












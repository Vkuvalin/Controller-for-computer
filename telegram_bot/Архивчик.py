""" Данное служит передачей значений между этапами """

# choice = None
# async with state.proxy() as data:
#     data['choice'] = choice

# choice = None
# async with state.proxy() as data:
#     mode = data['choice']
#     await message.answer('Возвращаю значение из предыдущего этапа (перенес)')
#     await message.answer(choice)
""" ---------------------------------------------- """


# Браузер
# import webbrowser
# webbrowser.open("https://codecamp.ru/blog/python-webbrowser-module/")


# Скриншот
# Вариант-1
# import pyautogui
# screen = pyautogui.screenshot('screenshot/screenshot.png')
#
# print(screen)

# Вариант-2
# import pyscreenshot
# def take_pic():
#       image = pyscreenshot.grab()
#       return image.show()
#
# print(take_pic())





#
# from pynput.mouse import Button, Controller
#
# mouse = Controller()
#
# # Считывание положения указателя
# print(f'Текущее положение указателя: {mouse.position}')
#
# # Установка положения указателя
# mouse.position = (10, 20)
# print(f'Указатель перемещен в позицию: {mouse.position}')
#
# # Перемещение указателя относительно текущего положения
# mouse.move(0, -10)
#
# # Нажатие и отпускание левой кнопки мыши
# mouse.press(Button.left)
# mouse.release(Button.left)
#
# # Двойной клик - отличается от простого нажатия
# mouse.click(Button.left, 2)
#
# # Прокрутка страницы на два шага вниз
# mouse.scroll(0, 2)
# https://www.youtube.com/watch?v=iZzx1keKztY
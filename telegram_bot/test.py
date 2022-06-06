# # coding=utf-8

from pynput.mouse import Button, Controller

mouse = Controller()

# # Считывание положения указателя
# print(f'Текущее положение указателя: {mouse.position}')
#
# # Установка положения указателя
# mouse.position = (10, 20)
# print(f'Указатель перемещен в позицию: {mouse.position}')

# # Перемещение указателя относительно текущего положения
# mouse.move(0, -100)

# # Нажатие и отпускание левой кнопки мыши
# mouse.press(Button.left)
# mouse.release(Button.left)
#
# # Двойной клик - отличается от простого нажатия
# mouse.click(Button.left, 2)
#
# Прокрутка страницы на два шага вниз
mouse.scroll(0, 20)


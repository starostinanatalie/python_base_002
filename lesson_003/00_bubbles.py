# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(100,100)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, width= 2)

# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
sd.sleep(3)
sd.clear_screen()

# TODO: начиная с 3го модуля мы стремимся соблюдать PEP8.
#     Перемеинуйте функцию bubble в слово/словосочетание, глагол, чтобы он отражал суть - "нарисовать пузырек".
#     Функции и методы должны носить названия-глаголы. А объекты - названия-существительные. И bubble сейчас как раз
#     больше похож на существительное, а должен быть похож на глагол/сказуемое.
def bubble(point, step, colour):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=colour, width=2)

point = sd.get_point(500,500)
bubble(point=point, step=7, colour=[216,53,225])

# Нарисовать 10 пузырьков в ряд
sd.sleep(3)
sd.clear_screen()
for x in range(100, 1001, 100):
    point = sd.get_point(x, 300)
    bubble(point=point, step=5, colour=[128,128,128])


# Нарисовать три ряда по 10 пузырьков
sd.sleep(3)
sd.clear_screen()
for y in range(120, 500, 130):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        bubble(point=point, step=5, colour=[128, 128, 128])


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
sd.sleep(3)
sd.clear_screen()
for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 10)

    # TODO: можете использовать sd.random_color(), чтобы получить случайный цвет.
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    bubble(point=point, step=step, colour=[red, green, blue])


# TODO: нажмите Ctrl + Alt + L, чтобы pyCharm "причесал" стиль кода.

sd.pause()

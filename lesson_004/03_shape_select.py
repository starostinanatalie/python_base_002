# -*- coding: utf-8 -*-

import simple_draw as sd
import math

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def draw_polygon(angles_quantity, initial_point, angle, length, width, colour):
    point = initial_point
    for _ in range(angles_quantity - 1):
        side = sd.get_vector(start_point=point, angle=angle, length=length)
        side.draw(color=colour, width=width)
        point = side.end_point
        angle = angle + (360 / angles_quantity)
    sd.line(side.end_point, end_point=initial_point, color=colour, width=width)

angle_quantity = int(input('Сколько углов у фигуры, которую Вы хотите нарисовать? '))
length = int(input('Введите длину стороны фигуры: '))
x = (sd.resolution[0] - length) / 2
delta_y = (length / (2 * math.sin(math.pi / angle_quantity))) * 2
y = (sd.resolution[1] - int(delta_y)) / 2
point = sd.get_point(x, y)

print('''Выберите цвет, которым Вы хотите нарисовать фигуру, из предложенных:
1. Желтый
2. Зеленый
3. Красный
4. Синий
5. Сиреневый
6. Голубой
7. Оранжевый
Введите номер выбранного цвета''')
colours = [sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_RED, sd.COLOR_DARK_BLUE, sd.COLOR_CYAN, sd.COLOR_BLUE,
                     sd.COLOR_ORANGE]
choise = 0
while choise not in [1, 2, 3, 4, 5, 6, 7]:
    print('Вы ввели некорректное значение')
    choise = int(input('''Выберите цвет, которым Вы хотите нарисовать фигуру, из предложенных:
    1. Желтый
    2. Зеленый
    3. Красный
    4. Синий
    5. Сиреневый
    6. Голубой
    7. Оранжевый
    Введите номер выбранного цвета: ''')) - 1
colour = colours[choise]
draw_polygon(angle_quantity,point, 0, length, 3, colour)


sd.pause()

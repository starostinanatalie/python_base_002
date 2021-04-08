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

# TODO: нужно все функции. Прямо использовать draw_pylygon нельзя.

# TODO: зачем 4 функции, когда можно использовать 1, которая умеет все это делать и даже может больше?
#  Цель этой задачи решить проблему "выбор 1 функции из набора функций" без 100500 if|else. Нужно будет создать список
#  функций, ожидать какой цвет и какую функцию выберет пользователь и использовать его выбор в качестве индекс по списку
#  .
#  Т.е. цель введенного ограничения: понять, что функции можно хранить/передавать как и другие объекты.

angle_quantity = int(input('Сколько углов у фигуры, которую Вы хотите нарисовать? '))
length = int(input('Введите длину стороны фигуры: '))
x = (sd.resolution[0] - length) / 2
delta_y = (length / (2 * math.sin(math.pi / angle_quantity))) * 2
y = (sd.resolution[1] - int(delta_y)) / 2
point = sd.get_point(x, y)

colours = [("1. Желтый", sd.COLOR_YELLOW),
           ("2. Зеленый", sd.COLOR_GREEN),
           ("3. Красный", sd.COLOR_RED),
           ("4. Синий", sd.COLOR_DARK_BLUE),
           ("5. Сиреневый", sd.COLOR_CYAN),
           ("6. Голубой", sd.COLOR_BLUE),
           ("7. Оранжевый", sd.COLOR_ORANGE)
           ]
choise = 0
print("Выберите цвет, которым Вы хотите нарисовать фигуру, из предложенных:")
for i in colours:
    print(i[0])
choise = int(input("Введите номер выбранного цвета: "))


while choise > len(colours) + 1:
    print('Вы ввели некорректное значение')
    print("Выберите цвет, которым Вы хотите нарисовать фигуру, из предложенных:")
    for i in colours:
        print(i[0])
    choise = int(input("Введите номер выбранного цвета: "))

colour = colours[choise - 1][1]
print(choise)
draw_polygon(angle_quantity,point, angle, length, 3, colour)


sd.pause()

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

# TODO: меню выводить с помощью цикла.
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
# TODO: изменить условие. Оно создает список из 7 элементов. А если их 100?
#  Зачем нам список из 100 элемента, и еще и сравнивать с каждым из них, если на нужно сранить только с последним?
#  Примечание: "not in" будет последовательно сранивать с 1, с 2, ... с 100500. В то время как мы можем сразу
#  сравнить choice < 100500
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

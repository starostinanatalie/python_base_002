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

def draw_triangle(initial_point, angle, side_length):
    angles_quantity = 3
    draw_polygon(angles_quantity, initial_point, angle, side_length, 3, colour)

def draw_square(initial_point, angle, side_length):
    angles_quantity = 4
    draw_polygon(angles_quantity, initial_point, angle, side_length, 3, colour)

def draw_pentagon(initial_point, angle, side_length):
    angles_quantity = 5
    draw_polygon(angles_quantity, initial_point, angle, side_length, 3, colour)

def draw_hexagon(initial_point, angle, side_length):
    angles_quantity = 6
    draw_polygon(angles_quantity, initial_point, angle, side_length, 3, colour)

def draw_septagon(initial_point, angle, side_length):
    angles_quantity = 7
    draw_polygon(angles_quantity, initial_point, angle, side_length, 3, colour)

# TODO: нужно все функции. Прямо использовать draw_pylygon нельзя.

# TODO: зачем 4 функции, когда можно использовать 1, которая умеет все это делать и даже может больше?
#  Цель этой задачи решить проблему "выбор 1 функции из набора функций" без 100500 if|else. Нужно будет создать список
#  функций, ожидать какой цвет и какую функцию выберет пользователь и использовать его выбор в качестве индекс по списку
#  .
#  Т.е. цель введенного ограничения: понять, что функции можно хранить/передавать как и другие объекты.

side_length = int(input('Введите длину стороны фигуры: '))

colours = [("1. Желтый", sd.COLOR_YELLOW),
           ("2. Зеленый", sd.COLOR_GREEN),
           ("3. Красный", sd.COLOR_RED),
           ("4. Синий", sd.COLOR_DARK_BLUE),
           ("5. Сиреневый", sd.COLOR_CYAN),
           ("6. Голубой", sd.COLOR_BLUE),
           ("7. Оранжевый", sd.COLOR_ORANGE)
           ]
choise_colour = 0
print("Выберите цвет, которым Вы хотите нарисовать фигуру, из предложенных:")
for i in colours:
    print(i[0])
choise_colour = int(input("Введите номер выбранного цвета: "))


while choise_colour > len(colours) + 1:
    print('Вы ввели некорректное значение')
    print("Выберите цвет, которым Вы хотите нарисовать фигуру, из предложенных:")
    for i in colours:
        print(i[0])
    choise_colour = int(input("Введите номер выбранного цвета: "))

colour = colours[choise_colour - 1][1]

point = sd.get_point(100,100)

polygons = [("1. Треугольник", draw_triangle(point, 0, side_length)),
           ("2. Квадрат", draw_square(point, 0, side_length)),
           ("3. Пятиугольник", draw_pentagon(point, 0, side_length)),
           ("4. Шестиугольник", draw_hexagon(point, 0, side_length)),
           ("5. Семиугольник", draw_septagon(point, 0, side_length)),
           ]

print("Выберите фигуру, которую Вы хотите нарисовать, из предложенных:")
for item in polygons:
    print(item[0])
choise_figure = int(input("Введите номер выбранной фигуры: "))

while choise_figure > len(colours) + 1:
    print('Вы ввели некорректное значение')
    print("Выберите фигуру, которую Вы хотите нарисовать, из предложенных:")
    for i in colours:
        print(i[0])
    choise_figure = int(input("Введите номер выбранной фигуры: "))

x = (sd.resolution[0] - side_length) / 2
delta_y = (side_length / (2 * math.sin(math.pi / (choise_figure + 2)))) * 2
y = (sd.resolution[1] - int(delta_y)) / 2
point = sd.get_point(x, y)

print(choise_figure)
print(type(polygons[choise_figure - 1][1]))

sd.pause()

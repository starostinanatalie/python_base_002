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

def draw_triangle(initial_point, angle, side_length, colour):
    angles_quantity = 3
    draw_polygon(angles_quantity, initial_point, angle, side_length, 3, colour)

def draw_square(initial_point, angle, side_length, colour):
    angles_quantity = 4
    draw_polygon(angles_quantity, initial_point, angle, side_length, 3, colour)

def draw_pentagon(initial_point, angle, side_length, colour):
    angles_quantity = 5
    draw_polygon(angles_quantity, initial_point, angle, side_length, 3, colour)

def draw_hexagon(initial_point, angle, side_length,colour):
    angles_quantity = 6
    draw_polygon(angles_quantity, initial_point, angle, side_length, 3, colour)

def draw_septagon(initial_point, angle, side_length, colour):
    angles_quantity = 7
    draw_polygon(angles_quantity, initial_point, angle, side_length, 3, colour)

side_length = int(input('Введите длину стороны фигуры: '))

colours = [("Желтый", sd.COLOR_YELLOW),
           ("Зеленый", sd.COLOR_GREEN),
           ("Красный", sd.COLOR_RED),
           ("Синий", sd.COLOR_DARK_BLUE),
           ("Сиреневый", sd.COLOR_CYAN),
           ("Голубой", sd.COLOR_BLUE),
           ("Оранжевый", sd.COLOR_ORANGE)
           ]
choise_colour = 0

while True:
    print("Выберите цвет, которым Вы хотите нарисовать фигуру, из предложенных:")
    for i, (name, colour) in enumerate(colours, 1):
        print(i, name)
    choise_colour = int(input("Введите номер выбранного цвета: "))


    if 0 >= choise_colour >= len(colours) + 1:
        print('Вы ввели некорректное значение')
    else:
        break
colour = colours[choise_colour - 1][1]

x = (sd.resolution[0] - side_length) / 2
y = (sd.resolution[1] - side_length * 2) / 2
point = sd.get_point(x, y)

polygons = [("Треугольник", draw_triangle),
           ("Квадрат", draw_square),
           ("Пятиугольник", draw_pentagon),
           ("Шестиугольник", draw_hexagon),
           ("Семиугольник", draw_septagon),
           ]

# (Natalie Starostina) Спасибо!!! Про функции поняла, очень классно!

choise_figure = 0

while True:
    print("Выберите фигуру, которую Вы хотите нарисовать, из предложенных: ")
    for i, figure in enumerate(polygons, 1):
        print(i, figure[0])
    choise_figure = int(input("Введите номер выбранной фигуры: "))

    # TODO: можно ввести 0 и программа упадет
    if choise_figure >= len(polygons) + 1:
        print('Вы ввели некорректное значение')
    else:
        break

delta_y = (side_length / (2 * math.sin(math.pi / (choise_figure + 1)))) * 2
y = (sd.resolution[1] - int(delta_y)) / 2
point = sd.get_point(x, y)

polygons[choise_figure - 1][1](point, 0, side_length, colour)

sd.pause()

# почти
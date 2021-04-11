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
    for i, colour in enumerate(colours):
        print(i + 1, colour[0])
    choise_colour = int(input("Введите номер выбранного цвета: "))
    if choise_colour > len(colours) + 1:
        print('Вы ввели некорректное значение')
    else:
        break
colour = colours[choise_colour - 1][1]

point = sd.get_point(100,100)

polygons = [("Треугольник", draw_triangle),
           ("Квадрат", draw_square),
           ("Пятиугольник", draw_pentagon),
           ("Шестиугольник", draw_hexagon),
           ("Семиугольник", draw_septagon),
           ]

# (Natalie Starostina) Спасибо!!! Про функции поняла, очень классно!

# TODO: рад помочь) Так конечно сделать, используя только draw_polygon логично, но нам нужен был этот крюк с
#  4мя функциями, чтоб понят: они тоже объекты, их можно даже внутри функции передать.

choise_figure = 0

while True:
    print("Выберите фигуру, которую Вы хотите нарисовать, из предложенных: ")
    # TODO: использовать сложный случай вложенной распаковки, как в примере в 02 задаче (на всякий пожарный, правильный
    #  ответ в конце файла).
    for i, figure in enumerate(polygons):   # TODO: если 2ым параметром в enumerate передадим, например, 100500, то i будет
        print(i + 1, figure[0])             #  начинаться с 100500, а не с нуля. Можно использовать, чтобы +1 не делать.
    choise_figure = int(input("Введите номер выбранного цвета: "))
    if choise_figure > len(polygons) + 1:
        print('Вы ввели некорректное значение')
    else:
        break

# TODO: такая же проблема с падением. вводим 6 и падаем.

x = (sd.resolution[0] - side_length) / 2
delta_y = (side_length / (2 * math.sin(math.pi / (choise_figure + 2)))) * 2
y = (sd.resolution[1] - int(delta_y)) / 2
point = sd.get_point(x, y)

polygons[choise_figure - 1][1](point, 0, side_length)

sd.pause()











# for i, (fig_name, fig_function) in enumerate(polygons):

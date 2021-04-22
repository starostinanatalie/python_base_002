# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

def draw_polygon(angles_quantity, initial_point, angle, length, width, colour):
    point = initial_point
    for _ in range(angles_quantity - 1):
        side = sd.get_vector(start_point=point, angle=angle, length=length)
        side.draw(color=colour, width=width)
        point = side.end_point
        angle = angle + (360 / angles_quantity)
    sd.line(side.end_point, end_point=initial_point, color=colour, width=width)

angle_quantity = int(input('Сколько углов у фигуры, которую Вы хотите нарисовать? '))
x = int(input('Введите координату x начальной точки (лучше не с краю, чтобы фигура поместилась): '))
y = int(input('Введите координату y начальной точки: '))
point = sd.get_point(x, y)
angle = int(input('Введите угол наклона всей фигуры: '))
length = int(input('Введите длину стороны фигуры: '))

colours = [("Желтый", sd.COLOR_YELLOW),
           ("Зеленый", sd.COLOR_GREEN),
           ("Красный", sd.COLOR_RED),
           ("Синий", sd.COLOR_DARK_BLUE),
           ("Сиреневый", sd.COLOR_PURPLE),
           ("Голубой", sd.COLOR_BLUE),
           ("Оранжевый", sd.COLOR_ORANGE)
           ]

choise = 0
print("Выберите цвет, которым Вы хотите нарисовать фигуру, из предложенных:")

#  Мы так делали в 03 модуле в задаче 05_store. Пример:
#   for good, part_number in goods.items():
#  .
#  goods.items() - это был список из кортежей. Прям как у нас.

# (Natalie Starostina) в третьем модуле goods был словарем, а у списка метода .items() нет.

while True:
    print("Выберите цвет, которым Вы хотите нарисовать фигуру, из предложенных:")

    for i, (name, colour) in enumerate(colours):
        print(i + 1, name)
    choise = int(input("Введите номер выбранного цвета: "))

    # TODO: можно ввести -100 и программа упадет
    if choise >= len(colours) + 1:
        print('Вы ввели некорректное значение')
    else:
        break

colour = colours[choise - 1][1]

draw_polygon(angle_quantity,point, angle, length, 3, colour)

sd.pause()

# почти
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
draw_polygon(angle_quantity,point, angle, length, 3, colour)

sd.pause()

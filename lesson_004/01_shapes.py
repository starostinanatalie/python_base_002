# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

def draw_polygon(angles_quantity, initial_point, angle, length, width, colour):
    point = initial_point
    for _ in range(angles_quantity - 1):
        side = sd.get_vector(start_point=point, angle=angle, length=length)
        side.draw(color=[212, 93, 225], width=1)
        point = side.end_point
        angle = angle + (360 / angles_quantity)
    sd.line(side.end_point, end_point=initial_point, color=[212, 93, 225], width=1)

def draw_triangle(initial_point, angle, side_length):
    angles_quantity = 3
    draw_polygon(angles_quantity, initial_point, angle, length, 3, [212, 93, 225])

def draw_square(initial_point, angle, side_length):
    angles_quantity = 4
    draw_polygon(angles_quantity, initial_point, angle, length, 3, [212, 93, 225])

def draw_pentagon(initial_point, angle, side_length):
    angles_quantity = 5
    draw_polygon(angles_quantity, initial_point, angle, length, 3, [212, 93, 225])

def draw_hexagon(initial_point, angle, side_length):
    angles_quantity = 6
    draw_polygon(angles_quantity, initial_point, angle, length, 3, [212, 93, 225])

def draw_septagon(initial_point, angle, side_length):
    angles_quantity = 7
    draw_polygon(angles_quantity, initial_point, angle, length, 3, [212, 93, 225])

x = int(input('Введите координату x начальной точки (лучше не с краю, чтобы фигура поместилась): '))
y = int(input('Введите координату y начальной точки: '))
point = sd.get_point(x, y)
angle = int(input('Введите угол наклона всей фигуры: '))
length = int(input('Введите длину стороны фигуры: '))

draw_triangle(point, angle, length)
draw_square(point, angle, length)
draw_pentagon(point, angle, length)
draw_hexagon(point,angle, length)
draw_septagon(point, angle, length)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()

# зачет!
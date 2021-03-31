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

# TODO: добавьте внутрь ф-ций циклы, чтобы внутри каждой ф-ции был цикл for. Т.е. вместо:
#       vector_1 = ....
#       vector_1.draw()
#       ...
#       vector_100500 = ....
#       vector_100500.draw()
#  .
#  Мы получим:
#       for angel in range(...):
#           ...

def draw_triangle(initial_point, angle, side_length):
    side_one = sd.get_vector(start_point=initial_point, angle=angle, length=side_length, width=5)
    side_one.draw(color=[212,93,225])
    side_two = sd.get_vector(start_point=side_one.end_point, angle=angle + 120, length=side_length, width=5)
    side_two.draw(color=[212, 93, 225])
    side_three = sd.get_vector(start_point=side_two.end_point, angle=angle + 240, length=side_length, width=5)
    side_three.draw(color=[212, 93, 225])

def draw_square(initial_point, angle, side_length):
    side_one = sd.get_vector(start_point=initial_point, angle=angle, length=side_length, width=5)
    side_one.draw(color=[212,93,225])
    side_two = sd.get_vector(start_point=side_one.end_point, angle=angle + 90, length=side_length, width=5)
    side_two.draw(color=[212, 93, 225])
    side_three = sd.get_vector(start_point=side_two.end_point, angle=angle + 180, length=side_length, width=5)
    side_three.draw(color=[212, 93, 225])
    side_four = sd.get_vector(start_point=side_three.end_point, angle=angle + 270, length=side_length, width=5)
    side_four.draw(color=[212, 93, 225])

def draw_pentagon(initial_point, angle, side_length):
    side_one = sd.get_vector(start_point=initial_point, angle=angle, length=side_length, width=5)
    side_one.draw(color=[212,93,225])
    side_two = sd.get_vector(start_point=side_one.end_point, angle=angle + 72, length=side_length, width=5)
    side_two.draw(color=[212, 93, 225])
    side_three = sd.get_vector(start_point=side_two.end_point, angle=angle + 144, length=side_length, width=5)
    side_three.draw(color=[212, 93, 225])
    side_four = sd.get_vector(start_point=side_three.end_point, angle=angle + 216, length=side_length, width=5)
    side_four.draw(color=[212, 93, 225])
    side_five = sd.get_vector(start_point=side_four.end_point, angle=angle + 288, length=side_length, width=5)
    side_five.draw(color=[212, 93, 225])

def draw_hexagon(initial_point, angle, side_length):
    side_one = sd.get_vector(start_point=initial_point, angle=angle, length=side_length, width=5)
    side_one.draw(color=[212,93,225])
    side_two = sd.get_vector(start_point=side_one.end_point, angle=angle + 60, length=side_length, width=5)
    side_two.draw(color=[212, 93, 225])
    side_three = sd.get_vector(start_point=side_two.end_point, angle=angle + 120, length=side_length, width=5)
    side_three.draw(color=[212, 93, 225])
    side_four = sd.get_vector(start_point=side_three.end_point, angle=angle + 180, length=side_length, width=5)
    side_four.draw(color=[212, 93, 225])
    side_five = sd.get_vector(start_point=side_four.end_point, angle=angle + 240, length=side_length, width=5)
    side_five.draw(color=[212, 93, 225])
    side_six = sd.get_vector(start_point=side_five.end_point, angle=angle + 300, length=side_length, width=5)
    side_six.draw(color=[212, 93, 225])


x = int(input('Введите координату x начальной точки (лучше не с краю, чтобы фигура поместилась): '))
y = int(input('Введите координату y начальной точки: '))
point = sd.get_point(x, y)
angle = int(input('Введите угол наклона всей фигуры: '))
length = int(input('Введите длину стороны фигуры: '))
draw_triangle(point, angle, length)
draw_square(point, angle, length)
draw_pentagon(point, angle, length)
draw_hexagon(point,angle, length)

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

# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

#
for y in range(0, 600, 50):
    slide_x = y % 100
    for x in range(slide_x, 1200, 100):
        left_bottom = simple_draw.get_point(x, y)
        right_top = simple_draw.get_point(x + 100, y + 50)
        simple_draw.rectangle(left_bottom=left_bottom, right_top=right_top, color=[216,53,225], width=1)


# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

simple_draw.pause()

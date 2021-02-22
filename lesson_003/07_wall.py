# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

height_screen = int(input('Введите высоту экрана: '))
width_screen = int(input('Введите ширину экрана: '))
height_brick = int(input('Введите высоту кирпича: '))
width_brick = int(input('Введите ширину кирпича: '))
simple_draw.resolution = (width_screen, height_screen)

for y in range(0, height_screen, height_brick):
    if y % (2 * height_brick) == 0:
        slide_x = 0
    else:
        slide_x = int(width_brick / 2)
    #  Подказка: для первого цикла будет удобно добавить еще enumerate (пример в конце);
    for x in range(slide_x, width_screen, width_brick):
        left_bottom = simple_draw.get_point(x, y)
        right_top = simple_draw.get_point(x + width_brick, y + height_brick)
        simple_draw.rectangle(left_bottom=left_bottom, right_top=right_top, color=[216,53,225], width=1)

# TODO: здесь вы можете использовать "enumerate()". Пример:
#       seasons = ['Spring', 'Summer', 'Fall', 'Winter']
#       for season_id, season_name in enumerate(seasons):
# 	        print(season_id, ' - ', season_name)
#   .
#   В результате будет выведено:
#       0 - 'Spring'
#       1 - 'Summer'
#       2 - 'Fall'
#       3 - 'Winter'

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

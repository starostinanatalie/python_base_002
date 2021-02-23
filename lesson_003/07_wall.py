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

# TODO: enumerate - вот тут можно было. Тогда "y % (2 * height_brick)" упростилось до "row % 2".
#  На всякий пожарный: enumerate - хорошая функция. Оптимизированная и популярная, по ней легко понять, что для
#  алгоритм важен индекс элемента (в нашем случае индекс определяет номер ряда кирпичной кладки). Т.е. добавление
#  enumerate(range(...)) - это не "городить огород", а вполне хорошая практика.
#  .
#  Но все добровольно. Если хочется без enumerate - можно и без, главное запомните что он есть, он полезный и
#  часто спасает положение.
for y in range(0, height_screen, height_brick):






    if y % (2 * height_brick) == 0:
        slide_x = 0
    else:
        slide_x = int(width_brick / 2)
    # TODO: дополнительно. Если if|else нужен только для того, чтобы прибавить/отнять какое-то число от исходного, то
    #  можно использовать тернальный оператор if|else. Пример:
    #               if some_condition:
    #                   a = 100
    #               else:                       			 # было
    #                   a = 200.
    #  .
    #               a = 100 if some_condition else 200       # стало
    #  .              ↑  ↑                          ↑
    #  Аналогично и +=, *=, -=, /=:
    #               a *= 4 if some_condition_2 else 2        # если ДА - умножим в 4 раза, если НЕТ - в 2 раза
    #  .               ↑ ↑                          ↑




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

# почти
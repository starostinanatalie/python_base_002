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


for row, y in enumerate(range(0, height_screen, height_brick)):
    slide_x = 0 if row % 2 == 0 else int(width_brick / 2)
    for x in range(slide_x, width_screen, width_brick):
        left_bottom = simple_draw.get_point(x, y)
        right_top = simple_draw.get_point(x + width_brick, y + height_brick)
        simple_draw.rectangle(left_bottom=left_bottom, right_top=right_top, color=[216,53,225], width=1)


simple_draw.pause()

# почти
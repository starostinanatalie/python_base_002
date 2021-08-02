# -*- coding: utf-8 -*-


# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

from Drawing import drawing_rainbow
from Drawing import drawing_tree
from Drawing import drawing_smile
from Drawing import drawing_snow
from Drawing import drawing_house

import simple_draw as sd

def drawing_sun(x, y, r):
    center = sd.get_point(x, y)
    sd.circle(center_position=center, radius=r - 30, color=sd.COLOR_YELLOW, width=0)
    for i in range(0, 12):
        end_point = sd.get_point(x + r * sd.sin(30 * i), y + r * sd.cos(30 * i))
        sd.line(start_point=center, end_point=end_point, color=sd.COLOR_YELLOW, width=10)

sd.resolution = (1200, 800)
drawing_house.draw_rural_house(200, 30, 400, 500, 40, 250, 200, sd.COLOR_DARK_ORANGE)
drawing_smile.smiles_draw(400, 200, colour=sd.COLOR_WHITE)
drawing_rainbow.drawing_rainbow(400, 0, 900)
drawing_sun(150, 650, 80)
drawing_tree.draw_tree(850, 0)
drawing_tree.draw_tree(900, 25)
drawing_tree.draw_tree(950, 10)
drawing_snow.draw_snowflakes(300, 120, 50)

sd.pause()






# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

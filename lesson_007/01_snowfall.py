# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.x = sd.random_number(10, 600)
        self.y = sd.random_number(500, 750)
        self.length = sd.random_number(10, 35)
        self.factor_a = sd.random_number(1, 10) * 0.1
        self.factor_b = sd.random_number(1, 10) * 0.1
        self.factor_c = sd.random_number(40, 80)
        self.color = sd.background_color

    def move(self):
        pass

    def draw(self):
        self.point = sd.get_point(self.x, self.y)
        self.color = sd.COLOR_WHITE
        sd.snowflake(self.point, self.length, self.color, self.factor_a, self.factor_b, self.factor_c)

    def can_fall(self):
        pass

    def clear_previous_picture(self):
        self.point = sd.get_point(self.x, self.y)
        self.color = sd.background_color
        sd.snowflake(self.point, self.length, self.color, self.factor_a, self.factor_b, self.factor_c)



    # TODO здесь ваш код


flake = Snowflake()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()

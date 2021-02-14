# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
slide_point = 0
for colour in rainbow_colors:
    slide_point += 5
    beginning_point = sd.get_point(45 + slide_point, 50)
    end_point = sd.get_point(345 + slide_point, 450)
    sd.line(start_point=beginning_point, end_point=end_point, color=colour, width=4)

# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

sd.sleep(3)
sd.clear_screen()
slide_point = 0
for colour in rainbow_colors:
    slide_point += 50
    center = sd.get_point(-100, -150)
    sd.circle(center_position=center, radius=400 + slide_point, color=colour, width=50)


sd.pause()

# зачет!
import simple_draw as sd

sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20
def draw_snowflakes(x, y, N):
    snowflakes = [{'x': sd.random_number(0, x),
                   'y': sd.random_number(0, y),
                   'length': sd.random_number(10, 30),
                   'factor_a': sd.random_number(1, 10) * 0.1,
                   'factor_b': sd.random_number(1, 10) * 0.1,
                   'factor_c': sd.random_number(40, 80)
                   } for n in range(N)]
    for snowflake in snowflakes:
        point = sd.get_point(snowflake['x'], snowflake['y'])
        sd.snowflake(point, snowflake['length'], sd.COLOR_WHITE, snowflake['factor_a'],
                 snowflake['factor_b'], snowflake['factor_c'])

def draw_snowflakes_falling():
    snowflakes = [{'x': sd.random_number(10, 1100),
                   'y': sd.random_number(500, 550),
                   'length': sd.random_number(10, 100),
                   'factor_a': sd.random_number(1, 10) * 0.1,
                   'factor_b': sd.random_number(1, 10) * 0.1,
                   'factor_c': sd.random_number(40, 80)
                   } for n in range(N)]
    delta_x = 0
    delta_y = 0
    while True:
        sd.clear_screen()
        for snowflake in snowflakes:
            delta_random = sd.random_number(-70, 10)
            delta_determine = 10 / snowflake['length']
            x = snowflake['x'] + delta_x + delta_random
            y = snowflake['y'] + delta_y * delta_determine
            point = sd.get_point(x, y)
            sd.snowflake(point, snowflake['length'], sd.COLOR_WHITE, snowflake['factor_a'],
                         snowflake['factor_b'], snowflake['factor_c'])
        sd.sleep(0.1)
        delta_y -= 10
        delta_x += 2
        if sd.user_want_exit():
            break


def draw_snowflakes_advanced():
    snowflakes_advanced = [{'x': sd.random_number(10, 1100),
                            'y': sd.random_number(550, 600),
                            'length': sd.random_number(10, 30),
                            'factor_a': sd.random_number(1, 10) * 0.1,
                            'factor_b': sd.random_number(1, 10) * 0.1,
                            'factor_c': sd.random_number(40, 70),
                            } for n in range(N)]
    delta_x = 0
    delta_y = 0
    while True:
        sd.start_drawing()
        for snowflake in snowflakes_advanced:
            point = sd.get_point(snowflake['x'], snowflake['y'])
            sd.snowflake(point, snowflake['length'], sd.COLOR_WHITE, snowflake['factor_a'],
                         snowflake['factor_b'], snowflake['factor_c'])
        sd.finish_drawing()
        sd.sleep(0.1)
        sd.start_drawing()
        delta_x = (delta_x + 5) % 10
        delta_y = (delta_y - 10) % 50
        for snowflake in snowflakes_advanced:
            y = snowflake['y']
            point = sd.get_point(snowflake['x'], y)
            colour = sd.COLOR_WHITE if y < 10 else sd.background_color
            sd.snowflake(point, snowflake['length'], colour, snowflake['factor_a'],
                         snowflake['factor_b'], snowflake['factor_c'])
            snowflake['x'] = snowflake['x'] + delta_x + sd.random_number(-10, 5)
            snowflake['y'] = snowflake['y'] - delta_y * (1 / snowflake['length'])
            if snowflake['y'] < 5:
                snowflake['y'] = sd.random_number(550, 600)
                snowflake['x'] = sd.random_number(10, 1000)
        sd.finish_drawing()
        if sd.user_want_exit():
            break

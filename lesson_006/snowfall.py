
import simple_draw as sd
snowflakes = []


def create_snowflakes(N):
    '''
    input int - quantity of snowballs
    change global list snowflakes - create this list
    '''
    global snowflakes
    snowflakes = [{'number': n,
                   'x': sd.random_number(10, 1100),
                   'y': sd.random_number(500, 550),
                   'length': sd.random_number(10, 50),
                   'factor_a': sd.random_number(1, 10) * 0.1,
                   'factor_b': sd.random_number(1, 10) * 0.1,
                   'factor_c': sd.random_number(40, 80)
                   } for n in range(N)]

def paint_color_snowflakes(color):
    '''
    input - list of three integer from 0 to 255 or sd.color
    without output, draw snowflakes on screen
    '''
    for snowflake in snowflakes:
        point = sd.get_point(snowflake['x'], snowflake['y'])
        sd.snowflake(point, snowflake['length'], color, snowflake['factor_a'],
                     snowflake['factor_b'], snowflake['factor_c'])

def shift_snowflakes():
    '''
    without input, uses global variable - list snowflakes
    without output, change global variable - list snowflakes, change values x and y
    '''
    pass

def get_numbers_of_bottom_snowflakes():
    '''
    without input, uses global variable - list snowflakes
    returns list of integer - numbers of falling snowflakes
    '''
    numbers_of_bottom_snowflakes = []
    for snowflake in snowflakes:
        if snowflake['y'] < 5:
            numbers_of_bottom_snowflakes.append(snowflake['number'])
    return numbers_of_bottom_snowflakes

def delete_snowflakes(numbers):
    '''
    input list of integer - numbers of falling snowflakes
    without output, changes global variables - list snowflakes, removes from it some items
    '''
    global snowflakes
    for n in numbers:
        snowflakes.remove(n)

def draw_snowflakes(N):
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


def draw_snowflakes_advanced(N):
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


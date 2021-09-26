
import simple_draw as sd
snowflakes = []


def create_snowflakes(N):
    '''
    input int - quantity of snowballs
    change global list snowflakes - create this list
    '''
    global snowflakes
    for n in range(N):
        snowflakes.append({'x': sd.random_number(10, 600),
                   'y': sd.random_number(500, 750),
                   'length': sd.random_number(10, 35),
                   'factor_a': sd.random_number(1, 10) * 0.1,
                   'factor_b': sd.random_number(1, 10) * 0.1,
                   'factor_c': sd.random_number(40, 80)
                   })


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
    global snowflakes
    delta_y = -20
    for snowflake in snowflakes:
        delta_random = sd.random_number(-2, 3)
        delta_determine = 10 / snowflake['length']
        snowflake['x'] = snowflake['x'] + delta_random
        snowflake['y'] = snowflake['y'] + delta_y * delta_determine

def get_numbers_of_bottom_snowflakes():
    '''
    without input, uses global variable - list snowflakes
    returns list of integer - numbers of falling snowflakes
    '''
    numbers_of_bottom_snowflakes = []
    for snowflake in snowflakes:
        if snowflake['y'] < 5:
            numbers_of_bottom_snowflakes.append(snowflakes.index(snowflake))
    return numbers_of_bottom_snowflakes

def delete_snowflakes(numbers):
    '''
    input list of integer - numbers of falling snowflakes
    without output, changes global variables - list snowflakes, removes from it some items
    '''
    global snowflakes
    for n in numbers:
        point = sd.get_point(snowflakes[n]['x'], snowflakes[n]['y'])
        sd.snowflake(point, snowflakes[n]['length'], sd.background_color, snowflakes[n]['factor_a'],
                     snowflakes[n]['factor_b'], snowflakes[n]['factor_c'])
        snowflakes.pop(n)




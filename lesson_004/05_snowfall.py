# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

def draw_snowflakes():
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
            # TODO: 'colour' не нужен. Его можно заменить локальной переменной внутри каждого цикла.
             'colour': sd.COLOR_WHITE
             } for n in range(N)]
    delta_x = 0
    delta_y = 0
    while True:
        sd.start_drawing()
        for snowflake in snowflakes_advanced:
            point = sd.get_point(snowflake['x'], snowflake['y'])
            # TODO: убираем, и в sd.snowflake сразу пишем sd.COLOR_WHITE
            snowflake['colour'] = sd.COLOR_WHITE
            sd.snowflake(point, snowflake['length'], snowflake['colour'], snowflake['factor_a'],
                             snowflake['factor_b'], snowflake['factor_c'])
        sd.finish_drawing()
        sd.sleep(0.1)
        sd.start_drawing()
        # TODO: Тут считаем delta_x и объединяем 2 цикл ниже.
        for snowflake in snowflakes_advanced:
            y = snowflake['y']
            point = sd.get_point(snowflake['x'], y)
            # TODO: аналогично и тут
            if y < 20:
                snowflake['colour'] = sd.COLOR_WHITE
            else:
                snowflake['colour'] = sd.background_color
            sd.snowflake(point, snowflake['length'], snowflake['colour'], snowflake['factor_a'],
                             snowflake['factor_b'], snowflake['factor_c'])
        sd.finish_drawing()
        delta_x += 1
        if delta_x > 20:
            delta_x = 10
        # TODO: "y" тоже надо ограничить. А то снегопад разгоняется до световых скоростей.
        delta_y -= 7

        # TODO: используйте оператор %, чтобы не использовать if. Пример:
        #  a = (a + 1) % 100        # "а" всегда меньше 100.


        # TODO: этот цикл можно совместить с циклом выше, чтобы уменьшить количество кода.
        for snowflake in snowflakes_advanced:
            snowflake['x'] = snowflake['x'] + delta_x + sd.random_number(-10, 0)
            snowflake['y'] = snowflake['y'] + delta_y * (1 / snowflake['length'])
            if snowflake['y'] < 5:
                snowflake['y'] = sd.random_number(550,600)
                snowflake['x'] = sd.random_number(10, 1000)
        if sd.user_want_exit():
           break

#raw_snowflakes()
draw_snowflakes_advanced()
sd.pause()

# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       изменить координата_у и запомнить её в списке по индексу
#       создать точку отрисовки снежинки по координатам
#       нарисовать снежинку белым цветом в этой точке
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла: полная очистка всего экрана - долгая операция.
# - использовать хак для стирания старого положения снежинки:
#       отрисуем её заново на старом месте, но цветом фона (sd.background_color) и она исчезнет!
# - использовать функции sd.start_drawing() и sd.finish_drawing()
#       для начала/окончания отрисовки кадра анимации
# - между start_drawing и finish_drawing библиотека sd ничего не выводит на экран,
#       а сохраняет нарисованное в промежуточном буфере, за счет чего достигается ускорение анимации
# - в момент вызова finish_drawing все нарисованное в буфере разом покажется на экране
#
# Примерный алгоритм ускоренной отрисовки снежинок
#   навсегда
#     начать рисование кадра
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     закончить рисование кадра
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

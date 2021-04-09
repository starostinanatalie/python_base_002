# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

def draw_snowflakes():
    # TODO: если списковое включение занимает больше 2 строк, стоит задуматься "а не сделать ли полноценный список?"
    snowflakes = [{'x': sd.random_number(10, 1100), 'y': sd.random_number(500, 550),
               'length': sd.random_number(10, 100), 'factor_a': sd.random_number(1, 10) * 0.1,
               'factor_b': sd.random_number(1, 10) * 0.1, 'factor_c': sd.random_number(40, 80)} for n in range(N)]

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
    snowflakes_advanced = [{'x': sd.random_number(10, 1100), 'y': sd.random_number(500, 550),
               'length': sd.random_number(10, 40), 'factor_a': sd.random_number(2, 10) * 0.1,
               'factor_b': sd.random_number(3, 10) * 0.1, 'factor_c': sd.random_number(40, 70)} for n in range(N)]

    delta_x = 0
    delta_y = 0
    while True:
        # TODO: Надо упростить.
        #  Тут точно такой же алгоритм как и выше, отличие только в одном:
        #   "sd.clear_screen()" будет заменен на отдельный цикл, задача которого - покрасить все снежинки цветом
        #   фона. Этот новый цикл не должен ничего знать от delta_random и не должен ничего никуда перемешать.
        #   Перемещением будет заниматься цикл ниже. Тогда код значительно упростится
        delta_random = [sd.random_number(-30,10) for n in range(len(snowflakes_advanced))]
        sd.start_drawing()
        for i, snowflake in enumerate(snowflakes_advanced):
            delta_determine = 10 / snowflake['length']
            x = snowflake['x'] + delta_x + delta_random[i]
            y = snowflake['y'] + delta_y * delta_determine
            point = sd.get_point(x, y)
            sd.snowflake(point, snowflake['length'], sd.COLOR_WHITE, snowflake['factor_a'],
                     snowflake['factor_b'], snowflake['factor_c'])
        sd.finish_drawing()
        sd.sleep(0.1)
        sd.start_drawing()
        for i, snowflake in enumerate(snowflakes_advanced):
            delta_determine = 10 / snowflake['length']
            x = snowflake['x'] + delta_x + delta_random[i]
            y = snowflake['y'] + delta_y * delta_determine

            # TODO: y-координаты упавших снежинок нужно менять на новые. Т.о. снегопад не дожлен кончаться.
            if y < 5 + snowflake['length']:
                continue
            point = sd.get_point(x, y)
            sd.snowflake(point, snowflake['length'], sd.background_color, snowflake['factor_a'],
                     snowflake['factor_b'], snowflake['factor_c'])
        sd.finish_drawing()
        delta_y -= 10
        delta_x += 5
        if sd.user_want_exit():
           break

#draw_snowflakes()
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

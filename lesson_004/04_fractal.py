# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длина ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

def draw_branches(initial_point, angle, branch_length):
    if branch_length < 10:
        return


    point_left = initial_point
    point_right = initial_point
    angle_left = angle - 30
    angle_right = angle + 30
    # TODO: что делает строка ниже?
    branch_length = branch_length
    # TODO: в целом, создание точек point_left и point_right тоже не обязательно. Достаточно подставить start_point

    left_branch = sd.get_vector(start_point=point_left, angle=angle_left, length=branch_length)
    left_branch.draw()
    right_branch = sd.get_vector(start_point=point_right, angle=angle_right, length=branch_length)
    right_branch.draw()
    point_left = left_branch.end_point
    point_right = right_branch.end_point
    branch_length = branch_length * 0.75
    draw_branches(point_left, angle_left, branch_length)
    draw_branches(point_right, angle_right, branch_length)

root_point = sd.get_point(300,0)
root = sd.get_vector(root_point, 90, 30)
root.draw()
draw_branches(root.end_point, 90, 100)

sd.sleep(5)
sd.clear_screen()

def draw_branches_advanced(initial_point, angle, branch_length):
    if branch_length < 5:
        return
    point_left = initial_point
    point_right = initial_point
    delta_angle = sd.random_number(30 - 30*0.4, 30 + 30*0.4)
    angle_left = angle - delta_angle
    angle_right = angle + delta_angle
    # TODO: Такой же вопрос. Строка ниже ничего не делает. Только место занимает.
    #  Вероятно добавлена, чтобы было симметрично. Мол есть: point/angle_left/right и нужен branch_length.
    #  Но лучше убрать point_left/right и branch_length в угоду компактному коду.
    branch_length = branch_length
    left_branch = sd.get_vector(start_point=point_left, angle=angle_left, length=branch_length)
    left_branch.draw()
    right_branch = sd.get_vector(start_point=point_right, angle=angle_right, length=branch_length)
    right_branch.draw()

    # TODO: и 2 строки ниже тоже стоит ужать. Добавьте комментарии над вызовами draw_branches_advanced, чтобы было
    #  понятно, где левая, а где правая ветка. И этого вполне будет достаточно
    point_left = left_branch.end_point
    point_right = right_branch.end_point
    delta_length = sd.random_number(-20, 20) * 0.01
    branch_length = branch_length * (0.75 + delta_length)
    draw_branches_advanced(point_left, angle_left, branch_length)
    draw_branches_advanced(point_right, angle_right, branch_length)

    # TODO: например:
    # draw_branches_advanced(initial_point=left_branch.end_point, angle=angle - delta_angle,branch_length=branch_length)

# TODO: итого
#  "branch_length = branch_length" - точно надо убрать.
#  Остальное оставляю на ваше усмотрение: рекомендую сделать выбор в сторону компактности кода. Нет, это не значит,
#  что нужно кинуть и написать все в 3х строках. Но по возможности, стоит сделать сокращения, как это показано
#  в примее выше.

root_point = sd.get_point(300,0)
root = sd.get_vector(root_point, 90, 30)
root.draw()
draw_branches_advanced(root.end_point, 90, 100)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()

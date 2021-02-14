# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя ни одной из операций деления: ни деления с плавающей точкой /, ни целочисленного деления //
# и взятия остатка %
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 370, 37
print(f'Целочисленное деление {a} на {b} дает', end = ' ')
div_result = 0
while a > b:
    a = a - b
    div_result += 1
print(div_result)

# TODO: 370 на 37 будет 10

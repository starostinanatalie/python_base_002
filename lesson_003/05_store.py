# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Каждая запись отображает сколько и по какой цене закупалось товаров.
#
# Задание: вывести суммарную стоимость каждого ВИДА товара на складе c помощью циклов
#
# Формат вывода:
#   <товар_1> - <кол-во_товара_1> шт, стоимость <общая_стоимость_товара_1> руб
#   <товар_2> - <кол-во_товара_2> шт, стоимость <общая_стоимость_товара_2> руб
#   <товар_4> - <кол-во_товара_3> шт, стоимость <общая_стоимость_товара_3> руб
#
# Например:
#   Стул - 1111 шт, стоимость 8888 руб
#   Диван - 2222 шт, стоимость 9999 руб
#   и так далее
#
# Алгоритм должен получиться приблизительно такой:
#
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе

for good in goods:
    # TODO: Для самого первого цикла можно применить .items().
    #  Пусть есть словарь phone_numbers, который хранит пары (имя и номер телефона):
    #       phone_numbers = {
    #           "дед": 89110001111,
    #           "репка": 89510002222,
    #           "жучка": 87770003333
    #       }
    #  Мы можем запустить цикл по ключу и значения сразу, используя .items():
    #       for name, phone_numb in phone_numbers.items():					       # name - это ключ словаря,
    #           print(f'Персонаж "{name}" имеет номер телефона {phone_numb}')      # phone_number - значение по этому ключу
    #  .
    #  в результате:
    #       Персонаж "дед" имеет номер телефона 89110001111
    #       Персонаж "репка" имеет номер телефона 89510002222
    #       Персонаж "жучка" имеет номер телефона 87770003333
    #  .
    #  Итого, мы имеем доступ сразу и к ключу, и к значению.



    print(f'{good} - ', end= '')
    quantity = 0
    cost = 0
    for n in store[goods[good]]:
        quantity += n['quantity']
        cost += n['price'] * n['quantity']

    # TODO Объединить 2 print`а в один.
    print(f'{quantity} шт, стоимость {cost} руб')



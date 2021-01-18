#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

from pprint import pprint

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}
moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']
moscow_to_london = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** 0.5
moscow_to_paris = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** 0.5
paris_to_london = ((paris[0] - london[0]) ** 2 + (paris[1] - london[1]) ** 2) ** 0.5

distances['Moscow'] = {}
distances['Moscow']['London'] = moscow_to_london
distances['Moscow']['Paris'] = moscow_to_paris
distances['London'] = {}
distances['London']['Moscow'] = moscow_to_london
distances['London']['Paris'] = paris_to_london
distances['Paris'] = {}
distances['Paris']['Moscow'] = moscow_to_paris
distances['Paris']['London'] = paris_to_london


print(distances)

moscow_paris = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** 0.5
london_paris = ((paris[0] - london[0]) ** 2 + (paris[1] - london[1]) ** 2) ** 0.5
moscow_london = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** 0.5

distances_2 = {
    'Moscow': {
        'London': moscow_london,
        'Paris': moscow_paris
    },
    'London': {
        'Moscow': moscow_london,
        'Paris': london_paris
    },
    'Paris': {
        'Moscow': moscow_paris,
        'London': london_paris
    }
}

print(distances_2)
#  Вы создали 3 пустых словаря внутри distances, а затем начали по 1ому добавлять в него ключи. Сделайте так:
#       ✅ 1. вначале высчитайте переменные (moscow_paris, london_paris, moscow_london);
#       2. инициализируйте словарь сразу при объявлении (ниже пример).
#  .
#  Представим, что у нас есть система управления умным домом, и в ней есть конфигурация по умолчанию. Конфигурции
#  обычно представлены внутри программы в виде словарей. При загрузке системы мы должны произвести инициализацию
#  конфигурации (т.е. установить стартовые значения для всех параметров: включен ли свет, выключена ли вода,
#  варится ли кофе, запускать робот-пылесос или нет, включить кондиционер или выключить), и причем установить параметры
#  для каждой комнаты в отдельности.
#  .
#  Итак, у нас 2 варианта инициализировать такую конфигурацию.
#  .
#  Первый способ (как сделано сейчас).
#  Строим словари по очереди. Запоминанием какой ключ что хранит. Чтобы понять структуру словаря -
#  его обязательно выводить в консоль каждый раз (чем больше словарь, тем сложнее его запомнить).
d_1 = dict()
d_1['room_x'] = {}
d_1['room_y'] = {}
d_1['room_z'] = {}
lst = (1,2,3)		# номера включенных ламп
d_1['room_x']['active_lamps'] = lst
d_1['room_y']['active_lamps'] = lst + (4,5)
d_1['room_z']['room_t'] = {}
d_1['room_z']['room_t']['f_start_robot'] = True
d_1['room_z']['f_conditioner'] = False
d_1['room_z']['active_lamps'] = [1]
# TODO: Второй способ (более удобный для чтения, делает тоже самое!)
#  Объявлеям и инициализируем словарь сразу. Премущество - структура всего словаря всегда перед глазами, и мы можем
#  что-то добавить или убрать (шанс что ошибемся и сотрем что-то не то - меньше). Особенно эффективно, если мы соблюдаем
#  стиль и ставим пробелы между уровнями вложенности.
lst = (1,2,3)		# номера включенных ламп
d_2 = {
    'room_x': {
        'active_lamps': lst
    },
    'room_y': {
        'active_lamps': lst + (4,5)
    },
    'room_z': {
        'room_t': {
            'f_start_robot': True
        },
        'f_conditioner': False,
        'active_lamps': [1]
    }
}

print(d_1 == d_2)
# TODO: задача - сделать создание словаря вторым способом)
#  Это сделает код компактнее и удобнее для понимания. Одного взгляда будет достаточно, чтобы понять, что хранится
#  в словаре и какую структуру он имеет. Особенно удобно, когда словарь имеет большой размер или используется в
#  качестве конфигурации.
#  .
#  В итоге для получения расстояния, например, между Москвой и Парижем должно использоваться выражения:
#  distances['Moscow']['Paris']
#  distances['Paris']['Moscow']        # оба доступны
#  .
#  Аналогично для все остальных связок: Лондон-Москва, Париж-Лондон и т.п.

# зачет!
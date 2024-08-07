# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Soil):
            return Dirt()
        else:
            return None


class Air:

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Soil):
            return Dust()
        else:
            return None

    def __str__(self):
        return 'Воздух'


class Fire:

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Soil):
            return Lava()
        else:
            return None

    def __str__(self):
        return 'Огонь'

class Soil:

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None

    def __str__(self):
        return 'Земля'

class Storm:

    def __str__(self):
        return 'Шторм'

class Steam:

    def __str__(self):
        return 'Пар'

class Dirt:

    def __str__(self):
        return 'Грязь'

class Lightning:

    def __str__(self):
        return 'Молния'

class Dust:

    def __str__(self):
        return 'Пыль'

class Lava:

    def __str__(self):
        return 'Лава'

print(Fire(), '+', Air(), '=', Fire() + Air())
print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Soil(), '=', Fire() + Soil())
print(Soil(), '+', Air(), '=', Soil() + Air())
print(Fire(), '+', Water(), '=', Fire() + Water())
print(Water(), '+', Soil(), '=', Water() + Soil())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
# зачет!

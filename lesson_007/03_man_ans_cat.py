# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint
from python_snippets import *

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness,
        )

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def shopping_for_cat(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой для кота'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cats_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def bring_cat(self, cat):
        cat.home = self.house
        self.shopping_for_cat()
        cprint('{} Подобрал кота, пришлось купить ему еды'.format(self.name), color='cyan')

    def clean_house(self):
        if self.house.dirt > 100:
            cprint('{} убрался в доме'.format(self.name), color='blue')
            self.house.dirt -= 100
            self.fullness -= 20

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.cats_food < 10:
            self.shopping_for_cat()
        elif self.house.dirt > 100:
            self.clean_house()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cats_food = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, кошачьей еды осталось {}, денег осталось {}, грязно на {} баллов'.format(
            self.food, self.cats_food, self.money, self.dirt
        )

class Cat:

    def __init__(self, name):
        self.name = name
        self.fullfilness = 20
        self.home = None

    def sleep(self):
        self.fullfilness -= 10
        cprint('Кот {} спит'.format(self.name), color='green')

    def eat(self):
        cprint('Кот {} ест'.format(self.name), color='green')
        self.fullfilness += 20
        self.home.cats_food -= 10

    def tear_wallpaper(self):
        cprint('Кот {} дерет обои'.format(self.name), color='magenta')
        self.fullfilness -= 10
        self.home.dirt += 5

    def __str__(self):
        return 'Кот - {}, сытость {}'.format(
            self.name, self.fullfilness,
        )

    def act(self):
        if self.fullness <= 0:
            cprint('Кот {} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2 or dice == 5:
            self.tear_wallpaper()
        else:
            self.sleep()

Pavel = Man(name='Паша')
Barsik = Cat(name='Барсик')
my_sweet_home = House()
Pavel.go_to_the_house(house=my_sweet_home)
Pavel.bring_cat()

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    Pavel.act()
    Barsik.act()
    print('--- в конце дня ---')
    print(Pavel)
    print(Barsik)
    print(my_sweet_home)


# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)

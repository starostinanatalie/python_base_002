# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.salary_history = 0
        self.food = 50
        self.food_history = 0
        self.fur_coats = 0
        self.dirt = 0
        self.food_for_cat = 30

    def become_dirt(self):
        self.dirt += 5

    def is_dirt(self):
        return self.dirt > 90


    def __str__(self):
        return 'Денег в тумбочке {}, еды в холодильнике {}, грязно на {}%'.format(self.money, self.food, self.dirt)

class Human:

    def __init__(self, name, house):
        self.name = name
        self.fullfilness = 30
        self.happiness = 100
        self.house = house

    def __str__(self):
        return '{}, сытость {}, счастья {}'.format(self.name, self.fullfilness, self.happiness)

    def pet(self):
        self.happiness += 5
        cprint('{} гладил кота'.format(self.name))

    def eat(self):
        if self.house.food > 30:
            self.fullfilness += 30
            self.house.food_history += 30
            self.house.food -=30
            cprint('{} поел, сытость {}'.format(self.name, self.fullfilness))
        else:
            self.fullfilness += self.house.food
            self.house.food_history += self.house.food
            self.house.food = 0
            cprint('{} поел, сытость {}'.format(self.name, self.fullfilness))

class Husband(Human):

    def __init__(self, name, house):
        super().__init__(name, house)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.house.is_dirt():
            self.happiness -= 10
        if self.fullfilness < 2:
            self.eat()
        elif self.happiness < 11:
            self.gaming()
        elif self.house.money < 150:
            self.work()
        else:
            dice = randint(1, 6)
            if dice == 1 or dice == 6:
                self.work()
            elif dice == 2:
                self.eat()
            elif dice == 5:
                self.pet()
            else:
                self.gaming()

    def work(self):
        self.house.money += 150
        self.house.salary_history += 150
        self.fullfilness -= 10
        cprint('{} работал'.format(self.name))

    def gaming(self):
        self.fullfilness -= 10
        self.happiness += 20
        cprint('{} играл в танчики'.format(self.name))

class Wife(Human):

    def __init__(self, name, house):
        super().__init__(name, house)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.house.is_dirt():
            self.happiness -= 10
        if self.fullfilness < 10:
            self.eat()
        elif self.house.food < 60:
            self.shopping()
        elif self.house.food_for_cat < 10:
            self.buy_food_for_cat()
        elif self.happiness < 11 and self.house.money > 350:
            self.buy_fur_coat()
        elif self.happiness < 11:
            self.pet()
        elif self.house.dirt > 80:
            self.clean_house()
        else:
            dice = randint(1, 6)
            if dice == 1:
                self.shopping()
            elif dice == 5:
                self.pet()
            elif dice == 6:
                self.buy_food_for_cat()
            elif dice == 2 and self.house.money > 350:
                self.buy_fur_coat()
            else:
                self.clean_house()

    def shopping(self):
        self.fullfilness -= 10
        if self.house.money > 70:
            self.house.food += 70
            self.house.money -= 70
            cprint('{} купила еды на неделю'.format(self.name))
        else:
            self.house.food += self.house.money
            self.house.money = 0
            cprint('{} купила еды на сколько денег хватило'.format(self.name))

    def buy_food_for_cat(self):
        self.fullfilness -= 10
        if self.house.money > 70:
            self.house.food_for_cat += 70
            self.house.money -= 70
            cprint('{} купила еды котам на неделю'.format(self.name))
        else:
            self.house.food_for_cat += self.house.money
            self.house.money = 0
            cprint('{} купила еды котам на сколько денег хватило'.format(self.name))

    def buy_fur_coat(self):
        self.fullfilness -= 10
        self.happiness += 60
        self.house.money -= 350
        self.house.fur_coats += 1
        cprint('{} купила шубу'.format(self.name))

    def clean_house(self):
        if self.house.dirt > 100:
            self.house.dirt -= 100
            cprint('{} убралась, сколько смогла'.format(self.name))
        else:
            self.house.dirt = 0
            cprint('{} убралась, теперь чисто'.format(self.name))
        self.fullfilness -= 10

class Cat():

    def __init__(self, name, house):
        self.name = name
        self.fullfilness = 30
        self.house = house

    def __str__(self):
        return 'Кот {}, сытость - {}'.format(self.name, self.fullfilness)

    def eat(self):
        if self.house.food_for_cat >= 10:
            self.fullfilness += 20
            self.house.food_for_cat -= 10
            cprint('{} поел от пуза'.format(self.name))

        else:
            self.fullfilness += self.house.food_for_cat * 2
            self.house.food_for_cat = 0
            cprint('{} ну поел'.format(self.name))

    def sleep(self):
        self.fullfilness -= 10
        cprint('{} спит'.format(self.name))

    def tear_wallpapers(self):
        self.fullfilness -= 10
        self.house.dirt += 5
        cprint('{} дерет обои'.format(self.name))

    def act(self):
        if self.fullfilness < 5:
            self.eat()
        else:
            dice = randint(1, 6)
            if dice == 1:
                self.tear_wallpapers()
            elif dice == 6:
                self.eat()
            else:
                self.sleep()


class Child(Human):

    def __init__(self,name, house):
        super().__init__(name, house)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullfilness < 10:
            self.eat()
        else:
            dice = randint(1, 6)
            if dice == 1:
                self.eat()
            else:
                self.sleep()

    def eat(self):
        if self.house.food > 10:
            self.fullfilness += 10
            self.house.food_history += 10
            self.house.food -=10
            cprint('{} поел, сытость {}'.format(self.name, self.fullfilness))
        else:
            self.fullfilness += self.house.food
            self.house.food_history += self.house.food
            self.house.food = 0
            cprint('{} поел, сытость {}'.format(self.name, self.fullfilness))

    def sleep(self):
        self.fullfilness -= 10
        cprint('{} поел, сытость {}'.format(self.name, self.fullfilness))



home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
kolya = Child(name='Коля', house=home)
barsik = Cat(name='Барсик', house=home)
murzik = Cat(name='Мурзик', house=home)

for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    barsik.act()
    murzik.act()
    home.become_dirt()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(barsik, color='cyan')
    cprint(murzik, color='cyan')
    cprint(home, color='cyan')
cprint('За год заработано денег - {}, съедено еды - {}, куплено шуб - {}'.format(home.salary_history,\
       home.food_history, home.fur_coats))
# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

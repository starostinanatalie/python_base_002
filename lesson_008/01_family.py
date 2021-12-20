# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


class House:

    def __init__(self):
        self.money = 100
        self.salary_history = 0
        self.food = 50
        self.food_history = 0
        self.fur_coats = 0
        self.dirt = 0
        self.food_for_cat = 30
        self.food_for_cat_history = 0
        self.cats = 0

    def become_dirt(self):
        self.dirt += 5

    def is_dirt(self):
        return self.dirt > 90


    def __str__(self):
        return 'Денег в тумбочке {}, котов {}, еды для людей {}, для котов {}, грязно на {}%'.format(self.money,
                                                                                                     self.cats,
                                                                                                     self.food,
                                                                                                     self.food_for_cat,
                                                                                                     self.dirt)
class Human:

    def __init__(self, name, house):
        self.name = name
        self.fullfilness = 30
        self.happiness = 100
        self.house = house

    def __str__(self):
        if not self.is_dead():
            return '{}, сытость {}, счастья {}'.format(self.name, self.fullfilness, self.happiness)
        else:
            return '{} уже умер'.format(self.name)

    def is_dead(self):
        return self.fullfilness < 0 or self.happiness < 10

    def pet(self):
        self.happiness += 5
        cprint('{} гладил кота'.format(self.name))

    def eat(self):
        if self.house.food > 30:
            self.fullfilness += 30
            self.house.food_history += 30
            self.house.food -= 30
            cprint('{} поел, сытость {}'.format(self.name, self.fullfilness))
        else:
            self.fullfilness += self.house.food
            self.house.food_history += self.house.food
            self.house.food = 0
            cprint('{} поел, сытость {}'.format(self.name, self.fullfilness))

class Husband(Human):

    def __init__(self, name, house, salary):
        super().__init__(name, house)
        self.salary = salary

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.house.is_dirt() and not self.is_dead():
            self.happiness -= 10
        if self.is_dead():
            cprint('{} умер'.format(self.name), color='red')
        elif self.fullfilness < 10:
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
        self.house.money += self.salary
        self.house.salary_history += self.salary
        self.fullfilness -= 10
        cprint('{} работал, заработал {}'.format(self.name, self.salary))

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
        if self.house.is_dirt() and not self.is_dead():
            self.happiness -= 10
        if self.is_dead():
            cprint('{} умер'.format(self.name), color='red')
        elif self.fullfilness < 10:
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
        if self.house.money > 350:
            self.house.food_for_cat += 350
            self.house.money -= 350
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

    cats = []
    def __init__(self, name, house):
        self.name = name
        self.fullfilness = 30
        self.house = house
        self.house.cats += 1
        Cat.cats.append(self.name)
        self.dead = False

    def __str__(self):
        if not self.dead:
            return 'Кот {}, сытость - {}'.format(self.name, self.fullfilness)
        else:
            return 'Кот {} уже умер'.format(self.name)

    def eat(self):
        if self.house.food_for_cat >= 10:
            self.fullfilness += 20
            self.house.food_for_cat -= 10
            self.house.food_for_cat_history += 10
            cprint('{} поел от пуза'.format(self.name), color='yellow')
        elif self.house.food_for_cat > 0:
            self.fullfilness += self.house.food_for_cat * 2
            self.house.food_for_cat_history += self.house.food_for_cat
            self.house.food_for_cat = 0
            cprint('{} ну поел'.format(self.name), color='yellow')
        elif self.fullfilness > 0:
            cprint('Для {} еды больше нет'.format(self.name))
        else:
            cprint('Для {} еды больше нет'.format(self.name))
            self.fullfilness -= 1

    def sleep(self):
        self.fullfilness -= 10
        cprint('{} спит'.format(self.name), color='yellow')

    def tear_wallpapers(self):
        self.fullfilness -= 10
        self.house.dirt += 5
        cprint('{} дерет обои'.format(self.name), color='yellow')

    def die(self):
        self.dead = True
        print(self.dead)
        Cat.cats.remove(self.name)
        self.house.cats -= 1
        cprint('{} умер'.format(self.name), color='red')

    def act(self):
        if self.dead:
            return
        elif self.fullfilness < 0:
            self.die()
        elif self.fullfilness < 5:
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
        if self.is_dead():
            cprint('{} умер'.format(self.name), color='red')
        elif self.fullfilness < 10:
            self.eat()
        else:
            dice = randint(1, 6)
            if dice == 1 or dice == 6:
                self.eat()
            else:
                self.sleep()

    def eat(self):
        if self.house.food > 10:
            self.fullfilness += 10
            self.house.food_history += 10
            self.house.food -= 10
            cprint('{} поел, сытость {}'.format(self.name, self.fullfilness))
        else:
            self.fullfilness += self.house.food
            self.house.food_history += self.house.food
            self.house.food = 0
            cprint('{} поел, сытость {}'.format(self.name, self.fullfilness))

    def sleep(self):
        self.fullfilness -= 10
        cprint('{} спит, сытость {}'.format(self.name, self.fullfilness))


cat_names = ['Барсик', 'Вася', 'Пушок', 'Маркиз', 'Мурзик', 'Кокс', 'Айсик', 'Хрюндель', 'Шизик', 'Багира']
home = House()
serge = Husband(name='Сережа', house=home, salary=randint(50, 401))
masha = Wife(name='Маша', house=home)
kolya = Child(name='Коля', house=home)
cats = [Cat(name=cat_name, house=home) for cat_name in cat_names[:9]]

for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='red')
    print(Cat.cats)
    serge.act()
    masha.act()
    kolya.act()
    for cat in cats:
        cat.act()
    home.become_dirt()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    for cat in cats:
        cprint(cat, color='blue')
    cprint(home, color='cyan')
cprint('За год заработано денег {} при зарплате {}, съедено еды {}, съедено еды котами {}, выжило котов {}, \
куплено шуб {}'.format(home.salary_history, serge.salary, home.food_history, home.food_for_cat_history,\
                               home.cats, home.fur_coats))


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


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

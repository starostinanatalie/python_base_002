#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Natalie', 'Ivan', 'Vadim', 'Boris', 'Sveta']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    ['Natalie', 156],
    ['Ivan', 172],
    ['Vadim', 168],
    ['Boris', 170],
    ['Sveta', 128]
]
print('Рост отца -', my_family_height[1][1], 'см')
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
all_height = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1] + my_family_height[4][1]
print('Общий рост моей семьи -', all_height, 'см')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

# зачет!
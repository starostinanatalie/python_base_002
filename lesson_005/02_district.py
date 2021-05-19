# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1.room1 import folks as fc1_1
from district.central_street.house1.room2 import folks as fc1_2
from district.central_street.house2.room1 import folks as fc2_1
from district.central_street.house2.room2 import folks as fc2_2
from district.soviet_street.house1.room1 import folks as fs1_1
from district.soviet_street.house1.room2 import folks as fs1_2
from district.soviet_street.house2.room1 import folks as fs2_1
from district.soviet_street.house2.room2 import folks as fs2_2

print('В этом районе живут:')
print(', '.join(fc1_1) + ';')
print(', '.join(fc1_2) + ';')
print(', '.join(fc2_1) + ';')
print(', '.join(fc2_2) + ';')
print(', '.join(fs1_1) + ';')
print(', '.join(fs1_2) + ';')
print(', '.join(fs2_1) + ';')
print(', '.join(fs2_2) + ';')


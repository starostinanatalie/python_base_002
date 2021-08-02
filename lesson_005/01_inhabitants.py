# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

from room_1 import folks as folks_room1
from room_2 import folks as folks_room2


print('В комнате room_1 живут:', end=' ')
for person in folks_room1:
    print(person, end=', ')
print()

print('В комнате room_2 живут:', end=' ')
for person in folks_room2:
    print(person, end='')
print()

# зачет!

# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

class LogParser:

    def __init__(self, filename):
        self.filename = filename
        self.stat = {}

    def read_log(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self.parse_log(line=line)

    def write_stat(self):
        with open(self.file_name, 'w', encoding='cp1251') as file:
            for key, value in self.stat:
                file.writelines(f'[ {key} ] {value}')

    def parse_log(self, line):
        pass

    def statistic(self):
        pass



# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году

# -*- coding: utf-8 -*-

import zipfile
import os
# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

class CharStatistic():

    def __init__(self, filename):
        self.file_name = filename
        self.statistic = {}

    def unzip_file(self, file):
        print('unzip file')
        zfile = zipfile.ZipFile(file, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename
        self.work_with_file()

    def draw_table(self):
        self.work_with_file()
        print('+----------+----------+')
        print(f'|{"буква":^10}|{"частота":^10}')
        print('+----------+----------+')
        for key, value in self.statistic.items():
            print(f'{key:^10}|{value:^10}|')
        print('+----------+----------+')

    def work_with_file(self):
        if self.file_name.endswith('.zip'):
            self.unzip_file(self.file_name)
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self.collect_stat(line=line)


    def collect_stat(self, line):
        for char in line:
            if char.isalpha():
                if char in self.statistic:
                    self.statistic[char] += 1
                else:
                    self.statistic[char] = 1


filename = "voyna-i-mir.txt.zip"
statistic = CharStatistic(filename)
statistic.draw_table()



# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию

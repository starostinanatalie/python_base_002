# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом


user_input = input('Введите, пожалуйста, номер месяца: ')
month = int(user_input)
print('Вы ввели', month)

# TODO: лучше заменить на проверку условия "больше равно 1 и меньше равно 12".
#  Упрощенная запись:
#   -123 < x <= 100500      # от -123 не включительно, до 100500 включительно
if month not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
   print('Вы ввели неправильный номер месяца. ')
else:
    days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    print(f'В {month} месяце - {days_in_month[month - 1]} дней')


# TODO: нажмите Ctrl + Alt + L, чтобы pyCharm "причесал" стиль (отступы малость поехали)

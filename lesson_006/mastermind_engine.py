from random import randint

number_list = []

def get_number():
    global number_list
    number = randint(1000,9999)
    divider = 1000
    for _ in range(4):
        number_list.append(number // divider)
        number = int(number % divider)
        divider = int(divider // 10)





def check_number(number):
    pass

get_number()

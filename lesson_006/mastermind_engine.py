from random import randint

number_list = []

def get_number():
    global number_list
    while True:
        number_list.clear()
        number = randint(1000,9999)
        divider = 1000
        for _ in range(4):
            number_list.append(number // divider)
            number = int(number % divider)
            divider = int(divider // 10)
        prove_set = set(number_list)
        if len(prove_set) == 4:
            break

def check_number(number):
    divider = 1000
    answer = {'Bulls': 0, 'Cows': 0}
    for i in range(4):
        if int(number // divider) == number_list[i]:
            answer['Bulls'] += 1
        elif int(number // divider) in number_list:
            answer['Cows'] += 1
        number = int(number % divider)
        divider = int(divider // 10)
    return answer







from random import randint

number_list = []

def get_number():
    '''
    Change global list number_list, create new number in appearance of list of figures
    '''
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
    '''
    input int guessed number
    returns dictionary with keys 'Bulls' and 'Cows' and values with quantity of them
    '''
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

def is_gamover(answer):
    '''
    input dictionary with keys 'Bulls' and 'Cows' and values with quantity of them
    returns boolean True if values of 'Bulls' == 4
    '''
    if answer['Bulls'] == 4:
        return True






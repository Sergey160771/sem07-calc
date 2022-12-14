import logger

num1 = ''
num2 = ''
sign = ''

def get_mode():
    print('С какими числами вы планируете работать?')
    mode = input('1. Рациональные\n2. Комплексные\nВведите 1 или 2: ')
    if mode == '1' or mode == '2':
        return int(mode)
    else:
        print('Ошибка! Введите 1 или 2.')

def get_data():
    global num1
    global sign
    global num2
    num1 = input('\nВведите первое число: ')
    sign = input('Введите операцию (+, -, *, /): ')
    num2 = input('Введите второе число: ')

    return num1, sign, num2

def view_data(result):
    res_str = f'{num1} {sign} {num2} = {result}'
    logger.add_to_log(res_str)
    print(res_str)
import logger

def get_mode():
    print('С какими числами вы планируете работать?\n')
    tmp = input('Введите цифру 0, если с комплексными, и цифру 1, если с рациональными:\n')
    if tmp == '1':
        return 1
    elif tmp == '0':
        return 0
    else:
        print('Ошибка! Введите 1 или 0.')

def get_data():
    global num1
    global sign
    global num2
    num1 = input('\nВведите первое число:\n')
    sign = input('Введите операцию (+, -, *, /):\n')
    num2 = input('Введите второе число:\n')

    return num1, sign, num2

def view_data(result):
    logger.add_to_log(f'Результат выражения {num1} {sign} {num2} = {result}\n')
    print(f'\nРезультат выражения {num1} {sign} {num2} = {result}')
def my_func(num, degree):
    return num ** degree


def my_func_cycle(num, degree):
    a = num
    for i in range(1, abs(degree)):
        num *= a
    return 1 / num


num = input('Введите положительное число')
degree = input('Введите отрицательное целое число')
while True:
    try:
        num = float(num)
        degree = int(degree)
        if num == 0:
            num = input('Введите положительное число. Оно не должно быть равно 0')
        elif degree == 0:
            degree = input('Введите отрицательное число. Оно не должно быть равно 0')
        elif num < 0 or degree > 0:
            num = abs(num)
            if degree < 0:
                break
            else:
                degree = -degree
                print(f'Необходимо было ввести положительное и отрицательное числа. Введеное числа были преобразовано:'
                      f'{num} {degree}')
                break
        else:
            print(f'Вы ввели цифры: {num} и {degree}')
            break
    except ValueError:
        num = input('Введите положительное число')
        degree = input('Введите отрицательное целое число')

answer = my_func(num, degree)
print(f'Получен результатчерез "**": {answer}')

answer_2 = my_func_cycle(num, degree)
print(f'Получен результат через цикл: {answer_2}')

def my_f(x, y):
    return x / y


result = None
num1, num2 = input('Введите делимое и делитель'), input()
try:
    num1, num2 = float(num1), float(num2)
    result = my_f(num1, num2)
except ValueError:
    print('Вы ввели символ!')
except ZeroDivisionError:
    print('Деление на ноль невозможно!')

print(f'{num1} / {num2} = {result}')


###########Вторая задача#####################

# Вариант 1
def name_f(name, surname, birth, city, email, phone):
    return (f'Данные пользователя: Имя: {name} Фамилия: {surname} Дата рождения: {birth} Город: {city} email: {email} '
            f'Номер телефона: {phone}')


# Вариант 2
def name_kwargs(**user_data):
    print(f"Данные пользователя: {user_data}")


print(name_f(name='Васлий', surname='Иванов', city='Гродно', phone=89204140266, email='dvsdvsd@mail.ru', birth='30.06'
                                                                                                               '.1985'))

print(name_kwargs(name="Васлий", surname="Иванов", birth="30.06.1985", city='Гродно', email='dvsdvsd@mail.ru',
                  phone='89204140266'))


###########Третья задача#####################
# Вариант 1
def my_func(first, second, third):
    a = [third, second, first]
    a.sort()
    num_max, num_max_2 = a.pop(), a.pop()
    return num_max + num_max_2


# Вариант 2
def my_func_1(first, second, third):
    if first < second:
        first, second = second, first
    if first < third:
        third, first = first, third
    if third > second:
        second, third = third, second
    return first + second


max_sum = my_func(2, 3, 1)
print(max_sum)

max_sum = my_func_1(1, 2, 3)
print(max_sum)

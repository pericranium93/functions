def my_f(x, y):
    return x / y


result = None
num1, num2 = int(input('Введите делимое и делитель')), int(input())
try:
    result = my_f(num1, num2)
except ZeroDivisionError:
    print('Деление на ноль невозможно!')
print(result)


################################
def name_f(name, surname, birth, city, email, phone):
    print(f'Данные пользователя: Имя: {name} Фамилия: {surname} Дата рождения: {birth} Город: {city} email: {email} '
          f'Номер телефона: {phone}')


def name_kwargs(**user_data):
    print(f"Данные пользователя: {user_data}")


name_f(name='Васлий', surname='Иванов', city='Гродно', phone=89204140266, email='dvsdvsd@mail.ru', birth='30.06.1985')

name_kwargs(name="Васлий", surname="Иванов", birth="30.06.1985", city='Гродно', email='dvsdvsd@mail.ru',
            phone='89204140266')


##################################
def my_func(first, second, third):
    a = [third, second, first]
    a.sort()
    num_max, num_max_2 = a.pop(), a.pop()
    return num_max + num_max_2


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

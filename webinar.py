# my_list = ['qwe', True, 100]
# for ind, value in enumerate(my_list, 1):
#     print(ind, value)

#######################
# def my_f(name, surname='Guest'):  # необязательный аргумент surname или surname=None
#     print(name, surname)
#
#
# my_f('Ivan')

########################
# def my_f(name, *args):  # выводит в виде кортежа все, что попало в args
#     print(name, args)
#
#
# my_f('Ivan', 1, 2, 3, 3, 4, 5)
# my_f('Ivan2', 2, 45, 6)

########################
# def my_f(name, surname, age):  # функция с именными параметрами
#     print(name, surname, age + 1)
#
#
# my_f(name='Ivan', age=23, surname='Ivanov')


##############################
# def my_f(name, **kwargs):  # функция с key ward argument выводит в виде словаря
#     print(name, kwargs)
#
#
# my_f('Ivan', age=23, surname='Ivanov')


##########################
# names = ['Artyom', 'Anton', 'Sergei', 'Joulia']
# ages = [52, 18, 35]
#
# for i in zip(names, ages):  # объединяет 2 переменные (кортежи), только для ИТЕРАТИВНЫХ объектов (по ним можно пройти циклом)
#     print(i)
#
# print(list(zip(names, ages)))  # объединяет 2 переменные в список, но внутри кортежи
# print(dict(zip(names, ages)))  # создает словарь


############################
# def my_f(x):
#     return x ** 2 + 10


# data = [1, 25, 3, -8, 15]
# new_list = []
# for i in data:
#     new_list.append(my_f(i))
# print(new_list)

# result = list(map(my_f, data))  # проходит итеративно по каждому объекту data функцией.
# print(result)


#######################
# def my_f(x):
#     return x > 0
#
#
# data = [1, 25, 3, -8, 15, -10]
# result = list(filter(my_f, data))  # проходит итеративно по каждому объекту data функцией, но оставляет те объекты,
# print(result)                      # которые True


#####################################
# data = [1, 25, 3, -8, 15, -10]
# result = list(map(lambda x: x ** 2 + 10, data))  # анонимная лямбда функция
# result = list(filter(lambda x: x > 0, data))
# result = lambda x: x ** 2 + 10, data
# print(result)
#
# ##########################
# print(list(range(1, -7, -2)))  # целые числа в диапазоне [1; -7) с шагом -2








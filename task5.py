def sum_elem(string):
    """
    Отфильтровывает значения по типу данных и возвращает сумму всех числовых значений списка.
    :param string: Список, введенный пользователем
    :return:
    """
    if 'q' in string:
        last = string.index('q')
        string = string[:last]
        string = list(filter(lambda x: type(x) == float, string))
        return sum(string)
    else:
        string = list(filter(lambda x: type(x) == float, string))
        return sum(string)


amount = 0.0
finish = False
while not finish:
    user_str = input('Введите вашу строку').split()
    for i, element in enumerate(user_str):
        try:
            user_str[i] = float(element)
        except ValueError:
            continue
    amount += sum_elem(user_str)
    print(f'Сумма всех числовых элементов = {amount}')
    finish = True if 'q' in user_str else False  # Почему-то не позволяет использовать без else



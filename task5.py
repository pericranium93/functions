amount = 0
while True:
    user_str = input('Введите вашу строку').split()
    for element in user_str:
        try:
            if element == 'q':
                break
        except ValueError:
            continue







    # for element in user_str:
    #     if element == 'q':
    #         break
    #     else:
    #         amount += float(element)
    # print(amount)

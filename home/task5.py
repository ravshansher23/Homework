from random import uniform


def transfer_list_in_str(list_in: list) -> str:
   str_out = ''
   for name in list_in:
       rub = str(int(name//1))
       cop = str(int(name%1*100))
       if len(rub) == 1:
           str_out += f'0{rub} руб.'
       else:
           str_out += f'{rub} руб.'

       if len(cop) == 1:
           str_out += f'0{cop} коп.'
       else:
           str_out += f'{cop} коп.'





   return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    my_list.sort()
    str_out = ''
    for name in list_in:
        rub = str(int(name // 1))
        cop = str(int(name % 1 * 100))
        if len(rub) == 1:
            str_out += f'0{rub} руб.'
        else:
            str_out += f'{rub} руб.'

        if len(cop) == 1:
            str_out += f'0{cop} коп.'
        else:
            str_out += f'{cop} коп.'

    return str_out

result_2 = sort_prices(my_list)

print(result_2)


def sort_price_adv(list_out: list) -> list:
    str_out = ''
    list_out = my_list
    list_out.sort(reverse=True)

    for name in list_out:
        rub = str(int(name // 1))
        cop = str(int(name % 1 * 100))
        if len(rub) == 1:
            str_out += f'0{rub} руб.'
        else:
            str_out += f'{rub} руб.'

        if len(cop) == 1:
            str_out += f'0{cop} коп.'
        else:
            str_out += f'{cop} коп.'

    return str_out





result_3 = sort_price_adv(my_list)
print(result_3)


def check_five_max_elements(list_in: list) -> list:
    my_list.sort(reverse=True)
    list_in = my_list[0:4]
    str_out = ''


    for name in list_in:
        rub = str(int(name // 1))
        cop = str(int(name % 1 * 100))
        if len(rub) == 1:
            str_out += f'0{rub} руб.'
        else:
            str_out += f'{rub} руб.'

        if len(cop) == 1:
            str_out += f'0{cop} коп.'
        else:
            str_out += f'{cop} коп.'

    return str_out

    list_out = ["список из пяти самых больших элементов"]
    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)
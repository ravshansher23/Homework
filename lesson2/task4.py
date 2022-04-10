def convert_name_extract(list_in: list) -> list:

    list_out = []
    for name in list_in:
        list_out.append(f'Привет {name.split()[-1].title()}!')
    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)
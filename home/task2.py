


def convert_list_in_str(list_in: list) -> str:
    list_inside = []
    str_out = ''
    for name in list_in:
        if name.isdigit():
            list_inside.extend(['"', name.zfill(2), '"'])
            str_out += f' "{name.zfill(2)}"'
        elif name[0] == '+' or name[0] == '-':
            list_inside.extend(['"', f'{name[0]}0{name[1:]}', '"'])
            str_out += f' "{name[0]}0{name[1:]}"'
        else:
            list_inside.append(name)
            str_out += f' {name}'
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)


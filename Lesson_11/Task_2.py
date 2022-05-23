class Check(Exception):
    def __init__(self, txt):
        self.txt = txt


def division():
    try:
        num_1 = int(input('Введите делимое: '))
        num_2 = int(input('Введите делитель: '))
        if num_2 == 0:
            return print(Check(f'Ошибка: на ноль делить нельзя'))
        else:
            div = num_1 / num_2
        return print(div)
    except ValueError:
        return print(f'Ввели не число')
    except Check as err:
        return err



division()
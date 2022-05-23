class Check_num(Exception):
    def __init__(self):
        pass



def start():
    num_list = []

    while True:
        try:
            try:
                num = int(input('Введите число: '))
                num_list.append(num)
                next = input('Продолжаем?(y/n): ')
                if next == 'n':
                    print(num_list)
                    break
            except ValueError:
                raise Check_num
        except Check_num:
            next = input('Продолжаем?(y/n): ')
            if next == 'n':
                print(num_list)
                break
            start()




start()
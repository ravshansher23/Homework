class Warehouse:
    def __init__(self):
        self.items = {}

class Office_equipment(Warehouse):
    def add_item(self):
        try:
            name = input(f'Введите наименование: ')
            price = int(input(f'Введите цену за ед: '))
            quantity = int(input(f'Введите количество: '))
            item = {name: [price, quantity]}
            self.items.update(item)
            print(self.items)
        except ValueError:
            print('Не верное значение!')


class Printer(Office_equipment):
    def action(self):
        print(f'Печатает...')


class Scaner(Office_equipment):
    def action(self):
        print(f'Сканирует...')


class Xerox(Office_equipment):
    def action(self):
        print(f'Копирует...')



p1 = Printer()
p1.add_item()
p1.action()
s1 = Scaner()
s1.add_item()
s1.action()
x1 = Xerox()
x1.add_item()
x1.action()
x1.add_item()

class Cell:
    def __init__(self, quant: int):
        self.quantity = '*' * quant
        print(f'Клетка состоящая из {quant} ячеек')

    def __add__(self, other):
        self.sum = self.quantity + other.quantity
        print(f'После слияния получилось: {self.sum} ячеек')

    def __sub__(self, other):
        if self.quantity > other.quantity:
            len_sub = len(self.quantity) - len(other.quantity)
            self.sub = '*' * len_sub
            print(f'После вычитания получилось: {self.sub} ячеек')
        else:
            print(f'не может быть отрицательное количество ячеек')
    def __mul__(self, other):
        len_mul = len(self.quantity) * len(other.quantity)
        self.mul = '*' * len_mul
        print(f'После умножения получилось: {self.mul} ячеек')

    def __floordiv__(self, other):
        len_div = len(self.quantity) // len(other.quantity)
        if round(len_div) != 0:
            self.div = '*' * round(len_div)
            print(f'После деления получилось: {self.div} ячеек')
        else:
            print(f'После деления получилось 0 ячеек')
    def make_order(self, quant):
        self.order = [self.quantity[i:i+quant] for i in range(0, len(self.quantity), quant)]
        self.order = str(self.order).replace(',', '\n')
        self.order = self.order.replace('[', '')
        self.order = self.order.replace(']', '')
        self.order = self.order.replace(' ', '')
        self.order = self.order.replace("'", '')
        print(f'Клетка:\n{self.order}')


num = Cell(10)
bum = Cell(30)
num + bum
num - bum
num * bum
num // bum
print()
bum.make_order(5)

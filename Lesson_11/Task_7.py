class Complex_num:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return f'Сумма чисел = {self.a + other.a} + {self.b + other.b} * i'
    def __mul__(self, other):
        return f'Произведение чисел = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'


sum = Complex_num(12, 3)
sum2 = Complex_num(10, 4)
print(sum + sum2)
print(sum * sum2)
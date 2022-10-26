# class Coat:
#     size = 0
#     def __init__(self, size):
#         self.size = size / 6.5 + 0.5
#     # def expenditure(self):
#     #     self.V = self.size
#         print(f'Расход материала на изготовление пальто = {self.size}')
#
# class Suit:
#     hight = 0
#     def __init__(self, hight):
#         self.hight = hight * 2 +0.3
#         #
#         # self.H = self.hight * 2 +0.3
#         print(f'Расход материала на изготовление костюма = {self.hight}')
class Clothes:
    hight = 0
    size = 0

    def coat(self, size):
        self.size = size / 6.5 + 0.5
        print(f'Расход материала на изготовление пальто = {self.size}')
    def suit(self, hight):
        self.hight = hight * 2 +0.3
        print(f'Расход материала на изготовление костюма = {self.hight}')

    def sum_material(self):
        sum = self.hight + self.size
        return f'Общий расход материала = {sum}'


clo = Clothes()
clo.coat(50)
clo.suit(100)
print(clo.sum_material())

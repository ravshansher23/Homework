

class Matrix():
    def __init__(self, first_row: list, s_row: list, warehouse: set):
        self.first_row = first_row
        self.s_row = s_row
        self.warehouse = warehouse
        self.warehouse.add(self)


    def __str__(self):
        return f'Матрица: \n{self.first_row}\n{self.s_row}'



    def __add__(self, other):
        row_new = []
        row_new_2 = []
        for i in range(len(self.first_row)):
            first_num = int(self.first_row[i]) + int(other.first_row[i])
            row_new.append(first_num)
            second_num = int(self.s_row[i]) + int(other.s_row[i])
            row_new_2.append(second_num)

        print(f'Новая матрица: \n{row_new}\n{row_new_2}')



row_1 = [1, 2, 3, 4]
row_11 = [2, 2, 3, 4]
row_22 = [6, 6, 7, 8]
row_2 = [5, 6, 7, 8]
matrix = set()
matrix_1 = set()
matrix_0 = Matrix(row_1, row_2, matrix)
matrix_2 = Matrix(row_22, row_11, matrix_1)
# print(matrix_1)

for mat in matrix:
    print(f'{mat}')
print()
for mat in matrix_1:
    print(f'{mat}')
print()
matrix_0 + matrix_2

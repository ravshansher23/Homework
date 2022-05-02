


class Worker:
    name = 'Dasha'
    surname = 'Sherzhanova'
    position = 'Robin'
    income = {'wage': 700, 'bonus': 300}

class Position(Worker):
    def get_full_name(self, name, surname):

        self.name = name
        self.surname = surname
        full_name = (f'{self.surname} {self.name}')
        print(full_name)

    def get_total_income(self, wage, bonus):
        self.income['wage'] = wage
        self.income['bonus'] = bonus
        total_income = int(super().income['wage']) + int(super().income['bonus'])
        print(f'{total_income}$')



d = Position()
e = d.get_full_name('Даша', 'Шержанова')
w = d.get_total_income(100, 112)
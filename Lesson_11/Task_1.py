class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def printing(cls, day_month_year):
        date_list = []
        for i in day_month_year.split():
            if i != '-':
                date_list.append(i)

        return f'{(date_list[0])}, {(date_list[1])}, {(date_list[2])}'

    @staticmethod
    def valid(day, month, year):
        if 0 < day < 32 and 0 < month < 13:
            if month == 2 and 0 < day < 29 and year % 4 != 0:
                month = str(month)
                return f'{day}.{month.zfill(2)}.{year}'
            elif year % 4 == 0 and month == 2 and 0 < day < 30 and year > 0:
                month = str(month)
                return f'{day}.{month.zfill(2)}.{year}'
            elif month != 2:
                month = str(month)
                return f'{day}.{month.zfill(2)}.{year}'

            else:
                return f'Не верно введена дата'

        else:
            return f'Не верно введена дата'



date = Date('12 - 2 - 1996')

print(date.printing('12 - 2 - 1996'))
print(Date.valid(28, 12, 1996))
print(Date.valid(29, 2, 1997))
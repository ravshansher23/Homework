
class Stationery:
    title = None
    def draw(self):
        if self.title is None:
            print(f'«Запуск отрисовки»')
        else:
            print(f'Запуск отрисовки {self.title}')



class Pen(Stationery):
    title = '"Ручка"'
class Pencil(Stationery):
    title = '"Карандаш"'
class Handle(Stationery):
    title = '"Маркер"'
draw_1 = Pen()
draw_2 = Pencil()
draw_3 = Handle()

f = draw_1.draw()
f1 = draw_2.draw()
f2 = draw_3.draw()

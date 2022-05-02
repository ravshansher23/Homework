

class Car:
    speed = 65
    color = 'Red'
    name = 'BMW'
    is_police = False

    def show_speed(self):
        print(f'Скорость = {self.speed} км/ч')
    def go(self):
        print(f'Машина поехала')
    def stop(self):
        print(f'Машина остановилась')

    def turn(self, direction):
        print(f'Машина направлена {direction}')
class TownCar(Car):
    def show_speed(self, speed):
        if speed > 60:
            print(f'Скорость = {speed} км/ч, вы превышаете скорость')
        else:
            print(f'Скорость = {speed} км/ч')
class SportCar(Car):
    def show_speed(self):
        print(f'Скорость = {self.speed} км/ч')
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость = {self.speed} км/ч, вы превышаете скорость')
        else:
            print(f'Скорость = {self.speed} км/ч')
class PoliceCar(Car):
    is_police = True
    if is_police == True:
        print(f'Это полицейская машина')




car_1 = PoliceCar()
car_p = car_1.show_speed()
car_p = car_1.go()
car_p = car_1.stop()
car_p = car_1.turn('прямо')


car_2 = SportCar()
car_s = car_2.go()
car_s = car_2.stop()
car_s = car_2.turn('налево')
car_s = car_2.show_speed()

car_3 = WorkCar()
car_s = car_3.go()
car_s = car_3.stop()
car_s = car_3.turn('направо')
car_s = car_3.show_speed()

car_4 = TownCar()
car_s = car_4.go()
car_s = car_4.stop()
car_s = car_4.turn('направо')
car_s = car_4.show_speed(100)
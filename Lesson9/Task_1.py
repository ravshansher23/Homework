import time

class TrafficLight():
    __color = ['Red', 'Yellow', 'Green']
    count = 0

    def frest(self):
        if self.count == 0:
            print(self.__color[0])
        elif self.count == 1:
            time.sleep(7)
            print(self.__color[1])
        elif self.count == 2:
            time.sleep(2)
            print(self.__color[2])
        TrafficLight.count += 1
    def running(self):
        run = TrafficLight()
        run.frest()
        run.frest()
        run.frest()

r = TrafficLight.running(self=0)




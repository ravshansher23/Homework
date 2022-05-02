class Road:
    _length = 0
    _width = 0

    def weight(self, length, width):
        self._length = length
        self._width = width
        mass_road = 25
        depth_road = 5
        weight = self._width * self._length * mass_road * depth_road
        print(f'Вес асфальта {weight} тонн')





r = Road()
d = r.weight(14, 16)
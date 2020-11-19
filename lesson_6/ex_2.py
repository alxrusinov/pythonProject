class Road:
    _normal_weight = 25
    _normal_height = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass(self):
        return self._width * self._length * self._normal_height * self._normal_weight


road_1 = Road(width=20, length=5000)

print(road_1.get_mass())

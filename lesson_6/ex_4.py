from random import randint
from itertools import count


class Car:
    _speed = 0
    _max_speed = 100

    def __init__(self, color, name, is_police):
        self.name = name
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f'this {self.name} is going')
        self._speed = randint(0, self._max_speed)

    def stop(self):
        print(f'this {self.name} stopped')

    def turn(self, direction):
        print(f'this {self.name} turned {direction}')

    def show_speed(self):
        print(f'current speed is {self._speed}')


class SportCar(Car):
    def __init__(self, color, name, is_police=False):
        super().__init__(color, name, is_police)


class PoliceCar(Car):
    def __init__(self, color, name, is_police=True):
        super().__init__(color, name, is_police)


class TownCar(Car):
    def __init__(self, color, name, is_police=False):
        super().__init__(color, name, is_police)

    def show_speed(self):
        super().show_speed()
        if self._speed > 60:
            print('You were speeding')


class WorkCar(Car):
    def __init__(self, color, name, is_police=False):
        super().__init__(color, name, is_police)

    def show_speed(self):
        super().show_speed()
        if self._speed > 40:
            print('You were speeding')


town_car = TownCar(name='Ford Focus', color='blue')
work_car = WorkCar(name='renault logan', color='gray')
sport_car = SportCar(name='Austin Martin', color='red')
police_car = PoliceCar(name='Lada Kalina', color='white')

print(town_car.color)
print(town_car.name)
print(town_car.is_police)
town_car.go()
town_car.show_speed()
town_car.turn('left')
town_car.turn('down')
town_car.stop()

print(sport_car.color)
print(sport_car.name)
print(sport_car.is_police)
sport_car.go()
sport_car.show_speed()
sport_car.turn('down')
sport_car.turn('up left')
sport_car.stop()

print(work_car.color)
print(work_car.name)
print(work_car.is_police)
work_car.go()
work_car.show_speed()
work_car.turn('left')
work_car.turn('left')
work_car.stop()

print(police_car.color)
print(police_car.name)
print(police_car.is_police)
police_car.go()
police_car.show_speed()
police_car.turn('down')
police_car.turn('down')
police_car.stop()


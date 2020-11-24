from time import sleep
from itertools import cycle


class TrafficLight:
    __color = {'RED': '\033[31m', 'YELLOW': '\033[33m', 'GREEN': '\033[32m'}
    __sleeping_time = {'RED': 7, 'YELLOW': 2, 'GREEN': 7}

    def running(self):
        for i in cycle(self.__color.keys()):
            print(f'\033[1m {self.__color[i]} {i}')
            sleep(self.__sleeping_time[i])


foo = TrafficLight()

foo.running()

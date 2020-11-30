from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calculate_cloth(self):
        pass


class Coat(Clothes):
    def __init__(self, V):
        self._V = V

    @property
    def calculate_cloth(self):
        return self._V / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, H):
        self._H = H

    @property
    def calculate_cloth(self):
        return self._H * 2 + 0.3


my_awesome_coat = Coat(50)
my_brutal_suit = Suit(1.8)

print(my_brutal_suit.calculate_cloth)
print(my_awesome_coat.calculate_cloth)
